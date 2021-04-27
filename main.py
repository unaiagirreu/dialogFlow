"""Install the following requirements:
    dialogflow        0.5.1
    google-api-core   1.4.1
"""
import os
import dialogflow
from google.api_core.exceptions import InvalidArgument

import logging
import requests
import json

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


'''
def start(update, context):
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'

    DIALOGFLOW_PROJECT_ID = 'unaibot-rheo'
    DIALOGFLOW_LANGUAGE_CODE = 'es'
    SESSION_ID = 'me'
    print(context)
    text_to_be_analyzed = "agur"

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    print("Fulfillment text:", response.query_result.fulfillment_text)
    update.message.reply_text('jon guapo!')'''

def echo(update, context):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'

    DIALOGFLOW_PROJECT_ID = 'unaibot-rheo'
    DIALOGFLOW_LANGUAGE_CODE = 'es'
    SESSION_ID = 'me'
    print(context)
    text_to_be_analyzed = update.message.text

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    print("Fulfillment text:", response.query_result.fulfillment_text)
    update.message.reply_text(response.query_result.fulfillment_text)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1677930408:AAENDo0ckRpJdHO8laGObV0MImmclBWXK6c", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # on different commands - answer in Telegram
    #dp.add_handler(CommandHandler("start", start))

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dp.add_handler(echo_handler)
    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    #dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()



if __name__ == '__main__':
    main()