import logging
from functools import lru_cache
from prompt import USER_PROMPT, SYSTEM_PROMPT
from utility import get_completion, pipeline_for_xml_parse


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) 

class AdGenerator:
    def __init__(self,business_details: str, keywords: str):
        self.business_details = business_details
        self.keywords = keywords
        self.ad = None

    def __call__(self):
        self.ad = self.generate_ad()
        if self.ad is None:
            return None
        try:
            return pipeline_for_xml_parse(self.ad)
        except Exception as e:
            logger.error(f"Can't parse ad\nException: {e}")
            return None
    
    def __str__(self):
        return f"AdGenerator(business_details={self.business_details}, keywords={self.keywords})"


    @lru_cache(maxsize=1000)
    def construct_messages(self) -> list[dict]:
        """
        Construct the system and user prompts for the OpenAI API.
        
        Args:
            business_details (str): The business details.
            keywords (str): The keywords.
        
        Returns:
            list: A list of dictionaries representing the system and user prompts.
        """
        logger.info(f"constructing messages")
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT.format(business_details=self.business_details, keywords=self.keywords)}
        ]
        logger.info(f"Finished constructing messages")
        return messages

    
    def generate_ad(self) -> str:
        """
        Generate a cover letter based on the provided job description and resume.
        Args:
            messages (list[dict]): The messages.
        
        Returns:
            str: The generated ad.
        """ 
        messages = self.construct_messages()
        if not isinstance(messages, list):
            logger.error("Can't construct messages")
            return None
     
        try:
            self.ad = get_completion(messages)
        except Exception as e:
            logger.error(f"Can't generate ad\nException: {e}")
            return None
        else:
            logger.info("successfully generated ad")
        return self.ad

