from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationSummaryBufferMemory
from dotenv import load_dotenv
import os

class service_provider:
    def __init__(self):
        load_dotenv()
        self.llm = ChatOpenAI(temperature=0.9, model="gpt-3.5-turbo")

    def create_llm(self):

        # Transportation Questions Keywords
        transportation_questions = [
            'When are you moving?',
            'Where are you moving to?',
            'Can I find you a moving company to assist your move? (Yes/No)',
            'What is most important to you in choosing a moving company? Are you more concerned with price or highest customer rating? (Price/Ratings)',
        ]
        
        # # Restaurant Recommendations Questions
        # restaurant_questions = [
        #     "What type of cuisine are you interested in trying?",
        #     "Do you have any dietary restrictions or preferences?",
        #     "Are you looking for a casual dining experience or something more formal?",
        #     "Do you prefer a restaurant with outdoor seating options?",
        #     "How important is the location of the restaurant to you?",
        #     "Are you interested in exploring local, independent restaurants or are you open to popular chains?",
        #     "Do you have a specific budget in mind for your dining experience?",
        #     "Are you celebrating a special occasion or just looking for a casual meal?"
        # ]

        # # Clinic Recommendations Questions
        # clinic_questions = [
        #     "What type of medical services are you seeking? (e.g., general practitioner, specialist, dental care, etc.)",
        #     "Are you looking for a clinic that accepts your insurance plan?",
        #     "How important is the location of the clinic to you?",
        #     "Are you seeking a clinic with specific amenities such as onsite lab testing or extended hours?",
        #     "Do you prefer a clinic with a particular focus, such as holistic health or traditional medicine?",
        #     "Are you interested in clinics that offer telemedicine or virtual appointments?",
        #     "Are you looking for a clinic with a specific language or cultural competency?",
        #     "Are there any specific medical conditions or concerns you would like the clinic to specialize in?"
        # ]


        # # Transportation Questions Keywords
        # transportation_questions = [
        #     "moving",
        #     "destination",
        #     "moving company",
        #     "criteria for choosing a moving company"
        # ]

        # # Restaurant Recommendations Keywords
        # restaurant_questions = [
        #     "cuisine",
        #     "dietary restrictions",
        #     "dining experience",
        #     "outdoor seating",
        #     "location importance",
        #     "independent vs. chains",
        #     "budget",
        #     "occasion"
        # ]

        # # Clinic Recommendations Keywords
        # clinic_questions = [
        #     "medical services",
        #     "insurance acceptance",
        #     "location importance",
        #     "clinic amenities",
        #     "medical focus",
        #     "telemedicine availability",
        #     "language/cultural competency",
        #     "specialized medical conditions"
        # ]
        
        transportation_desc = "When I say help door to door we can help you with the entire moving process from packing to applying for a home loan. We can even help you find a job or new local doctors. If is something that happens when you move we’ve got your back!"
        # restaurant_desc = "Looking for a place to dine? Let us help you discover the perfect restaurant experience tailored to your preferences! Whether you're craving a specific cuisine, seeking a cozy spot with outdoor seating, or aiming for a fine dining experience, we've got you covered. Just let us know your preferences, and we'll recommend the best spots in town to satisfy your culinary cravings."
        # clinic_desc = "Need medical assistance? Whether you're looking for a general practitioner, specialist, or dental care, we're here to help you find the right clinic to meet your healthcare needs. From convenient locations to specialized services and insurance acceptance, we'll guide you to the best clinics in town. Your health is our priority, so let us assist you in finding the perfect medical care provider for you."

        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    f"""
You are Geppetto, a friendly AI assistant designed to assist users. 

Here are the rules you must follow:

1. You must ask only one question at a time.
2. Always rephrase the questions to be more friendly.
3. You must Always start the conversation by introducing yourself and asking for the user's name only nothing else.
4. After Getting the name you should ask if they need assistance moving?
5. You only ask the user once in the start if they need assistance and never again.
6. If the sure says they want assistance provide the service description given below.
7. You Must always acknowledge user's message along with a response while asking the next question.
8. You must provide the service description from the options below and then ask, 'To get started, we will need to get some details. Is now a good time?'
9. If the user has answered any question before you asked it, skip that question.
10. When all questions have been asked, rephrase and provide a response similar to this: 'We will now go do the research for the best provider and get back to you when we have the information.'
11. If you don't know anything related to user ’s request, provide this response: "Since you are using Geppetto as a demo, we will not actually be following up with you. However, for a small investment, this functionality will soon be ready for you! Geppetto just needs a few more strings to complete the puppet. Boy, have strings gotten really expensive these days!"


Service descriptions:
For Transportation/Moving use: "{transportation_desc}"

Here are some instructions based on the user's response:
- If and only if the user asks when Geppetto will reach back or when they can expect a response back, respond with this: "Since you are using Geppetto as a demo, we will not actually be following up with you. However, for a small investment, this functionality will soon be ready for you! Geppetto just needs a few more strings to complete the puppet. Boy, have strings gotten really expensive these days!"
- If the user doesn't provide their name, acknowledge their decision and move on to ask about the services.
- If the user responds 'no' to any question, acknowledge their response and inform them to reach out if they need assistance in the future.

Here are the questions you can ask:
Transportation/Moving : "{transportation_questions}"

"""
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("""{text}""")
            ]
        )

        memory = ConversationSummaryBufferMemory(llm=self.llm, max_token_limit=700, memory_key="chat_history", return_messages=True)
        conversation = LLMChain(
            llm=self.llm,
            prompt=prompt,
            verbose=True,
            memory=memory
        )

        return conversation
    
"""
4. You provide assistance focusing on three services: door-to-door transportation, finding clinics or doctors, and recommending restaurants in the new location.


For Clinic/Hospital use: "{clinic_desc}"
for Restaurant use: "{restaurant_desc}"

Clinic/Hospital : "{clinic_questions}"
Restaurant : "{restaurant_questions}"
"""


class service_register:
    def __init__(self):
        load_dotenv()
        self.llm = ChatOpenAI(temperature=0.9, model="gpt-3.5-turbo")

    def create_llm(self):

        transportation_questions = [
            'What factors do you need to determine a price?',
            'How much notice to you need to deliver the services?',
        ]

        transportation_desc = "When I say help door to door we can help you with the entire moving process from packing to applying for a home loan. We can even help you find a job or new local doctors. If is something that happens when you move we’ve got your back!"
        # restaurant_desc = "Looking for a place to dine? Let us help you discover the perfect restaurant experience tailored to your preferences! Whether you're craving a specific cuisine, seeking a cozy spot with outdoor seating, or aiming for a fine dining experience, we've got you covered. Just let us know your preferences, and we'll recommend the best spots in town to satisfy your culinary cravings."
        # clinic_desc = "Need medical assistance? Whether you're looking for a general practitioner, specialist, or dental care, we're here to help you find the right clinic to meet your healthcare needs. From convenient locations to specialized services and insurance acceptance, we'll guide you to the best clinics in town. Your health is our priority, so let us assist you in finding the perfect medical care provider for you."

        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    f"""
You are Geppetto, a friendly AI assistant designed to assist users. 

Here are the rules you must follow:

1. You must ask only one question at a time.
2. Always rephrase the questions to be more friendly.
3. You must Always start the conversation by introducing yourself with this message "Hello, I’m Geppetto an
Intelligent AI referral partner and I believe I have a new customer for you, No strings attached.
Are you the right person for me to discuss this referral with or is there someone else I need to speak with?
"
4. Acknowledges they are the person to speak with and tells them" We have a customer for you and we want to ask few questions to make sure you are a good fit?"
5. If the user deviates from these services, provide a friendly response and after three messages without any relation to the services politely inform them that you can only assist with the service. 
6. If the user has answered any question before you asked it, skip that question.
7. When all questions have been asked, rephrase and provide a response similar to this: 'We will communicate with the customer and get back to you when they are ready to move forward.'

Here are some instructions based on the user's response:
- If and only if the user asks when Geppetto will reach back or when they can expect a response back, respond with this: "Since you are using Geppetto as a demo, we will not actually be following up with you. However, for a small investment, this functionality will soon be ready for you! Geppetto just needs a few more strings to complete the puppet. Boy, have strings gotten really expensive these days!"
- Otherwise, provide a response as you see fit according to the ongoing conversation.
- If the user responds with 'no' or refuses to any question, acknowledge their response and inform them to reach out if they need assistance in the future.

Here are the questions you can ask:
Transportation/Moving : "{transportation_questions}"

"""
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("""{text}""")
            ]
        )

        memory = ConversationSummaryBufferMemory(llm=self.llm, max_token_limit=700, memory_key="chat_history", return_messages=True)
        conversation = LLMChain(
            llm=self.llm,
            prompt=prompt,
            verbose=True,
            memory=memory
        )

        return conversation
    

"""

For Clinic/Hospital use: "{clinic_desc}"
for Restaurant use: "{restaurant_desc}"

Clinic/Hospital : "{clinic_questions}"
Restaurant : "{restaurant_questions}" 

"""