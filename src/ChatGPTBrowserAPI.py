import requests
import json
from urllib.parse import urljoin

from typing import (
    Any,
    List,
    Optional,
)
from langchain.callbacks.manager import AsyncCallbackManagerForLLMRun

from langchain.llms.base import BaseLLM
from langchain.schema import Generation, LLMResult

from langchain.callbacks.manager import (
    AsyncCallbackManagerForLLMRun,
    CallbackManagerForLLMRun,
)

class BrowserChatGPT(BaseLLM):

    chatgpt_web_api_url: str = "http://localhost:3000"
    
    def __new__(cls, **data: Any):  # type: ignore
        """Initialize the object."""
        return super().__new__(cls)

    @property
    def _llm_type(self) -> str:
        """Return type of llm."""
        return "chatgptscraped"

    def _generate(
        self,
        prompts: List[str],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> LLMResult:
        headers = {"Content-Type": "application/json"}
        payload = {"prompt": prompts[0]}
        response = requests.post(urljoin(self.chatgpt_web_api_url, "run"), headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            data = response.json()
            LLMResult(
                generations=[
                    [Generation(text=data)]
                ]
            )

        else:
            # API call failed
            raise ValueError(f"API call failed with status code {response.status_code}")

       
    
    def _agenerate(self, prompts: List[str], stop: List[str] | None = None, run_manager: AsyncCallbackManagerForLLMRun | None = None) -> LLMResult:
        return LLMResult(
                generations=[
                    [Generation(text=f"TODO {prompts[0]}")]
                ]
            )
    

