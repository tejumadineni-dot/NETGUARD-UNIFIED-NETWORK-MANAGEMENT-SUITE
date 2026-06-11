package com.netguard;

/*
 * Message Model Class
 * Used to transfer firewall/VLAN requests
 */
public class Message {

    private String type;
    private String content;

    // Default Constructor
    public Message() {
    }

    // Parameterized Constructor
    public Message(String type, String content) {
        this.type = type;
        this.content = content;
    }

    // Getter for type
    public String getType() {
        return type;
    }

    // Setter for type
    public void setType(String type) {
        this.type = type;
    }

    // Getter for content
    public String getContent() {
        return content;
    }

    // Setter for content
    public void setContent(String content) {
        this.content = content;
    }

    @Override
    public String toString() {
        return "Message [type=" + type + ", content=" + content + "]";
    }
}