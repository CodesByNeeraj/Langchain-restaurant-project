from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 
from langchain.chains import SequentialChain
from secret_key import openapi_key
import os 

llm = OpenAI(temperature=0.7,openai_api_key=openapi_key)
def generate_restaurant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(input_variables = ['cuisine'],
                                     template = "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.")
    
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name,output_key="restaurant_name")
    
    prompt_template_items = PromptTemplate(input_variables = ["restaurant_name"],
                                     template = "Suggest some menu items for {restaurant_name}. Return it as a comma seperated list.")

    food_items_chain = LLMChain(llm=llm,prompt=prompt_template_items,output_key="menu_items")
    
    chain = SequentialChain(chains = [name_chain,food_items_chain],input_variables=['cuisine'],output_variables=['restaurant_name','menu_items'],verbose=True)
    
    response = chain({'cuisine':cuisine})
    
    return response

if __name__=="__main__":
    print(generate_restaurant_name_and_items("Indian"))
    
    

     
    
    
    
    
    
    
    
    
