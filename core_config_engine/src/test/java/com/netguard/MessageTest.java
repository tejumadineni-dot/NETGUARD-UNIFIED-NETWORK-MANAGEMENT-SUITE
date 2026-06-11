package com.netguard;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

/*
 * Unit Test Class for Message
 */
public class MessageTest {

    /*
     * Test Message Object Creation
     */
    @Test
    public void testMessageCreation() {

        // Create Message Object
        Message message =
                new Message(
                        "FIREWALL",
                        "ALLOW ALL");

        // Verify Type
        assertEquals(
                "FIREWALL",
                message.getType());

        // Verify Content
        assertEquals(
                "ALLOW ALL",
                message.getContent());
    }
}