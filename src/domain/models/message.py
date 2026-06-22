from pydantic import BaseModel, Field

class Message(BaseModel):
    """ Represents a message in the conversation. """
    role: str = Field(..., description="The role of the message sender", examples=["user", "assistant"])
    content: str = Field(..., description="The content of the message", examples=["Hello, how can I help you?"])
    
class ChatHistory(BaseModel):
    """ Represents the chat history as a list of messages. """
    messages: list[Message] = Field(description="A list of messages in the conversation", default_factory=list)
    
    
    def add_message(self, role: str, content: str) -> None:
        """ Adds a new message to the chat history. """
        self.messages.append(Message(role=role, content=content))
        
    def to_langchain_list(self) -> list[dict[str, str]]:
        """ Converts the chat history to a format compatible with LangChain. """
        return [{"role": message.role, "content": message.content} for message in self.messages]
    
    @classmethod
    def from_langchain_list(cls, messages: list[dict[str, str]]) -> "ChatHistory":
        """ Creates a ChatHistory instance from a list of messages in LangChain format. """
        chat_history = cls(messages=[])
        for message in messages:
            chat_history.add_message(role=message["role"], content=message["content"])
        return chat_history