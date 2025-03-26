import json
import argparse
import logging
from pathlib import Path
from src.llm.llm_model import LLMModel
from src.llm.llm_prompt import PromptBuilder
from src.utils.config_utils import load_config
from src.schemas.user_schemas import UserMessageStatus
from langchain.output_parsers import PydanticOutputParser

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

CONFIG = load_config()


class PromptService:
    def __init__(
        self,
        config_path: str = "llm_prompt.json",
        experiment_id: str = "experiment_1",
    ):
        self.config_path = Path(config_path)
        self.experiment_id = experiment_id
        self.prompt_config = self._load_prompt_config()
        self.prompt_builder = self._init_prompt_builder()
        self.parser = PydanticOutputParser(pydantic_object=UserMessageStatus)

    def _load_prompt_config(self) -> dict:
        with self.config_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data[self.experiment_id]

    def _init_prompt_builder(self) -> PromptBuilder:
        return PromptBuilder(
            system_instructions=self.prompt_config["system_instructions"],
            prompt=self.prompt_config["prompt"],
        )

    def build_prompt(self, message: str) -> str:
        self.prompt_builder.add_variables(
            {
                "question": message,
                "format_instructions": self.parser.get_format_instructions(),
            }
        )
        return self.prompt_builder.build_prompt()

    def parse_response(self, raw_response: str):
        return self.parser.parse(raw_response)


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a user's emotional message."
    )
    parser.add_argument(
        "message", type=str, help="The user's message to analyze."
    )
    args = parser.parse_args()

    llm = LLMModel()
    service = PromptService(
        config_path=CONFIG["prompt"]["path"],
        experiment_id=CONFIG["prompt"]["experiment_id"],
    )
    formatted_prompt = service.build_prompt(args.message)

    print("\n🔹 Prompt Sent to LLM:\n", formatted_prompt)

    response = llm.generate_response(
        formatted_prompt,
        max_tokens=CONFIG["model"]["max_tokens"],
        temperature=CONFIG["model"]["temperature"],
    )

    print("\n🔹 Raw Response:\n", response)

    try:
        parsed = service.parse_response(response)
        print("\n Parsed Response:\n", parsed)
    except Exception as e:
        print(f"\n Error parsing response: {e}")


if __name__ == "__main__":
    main()
