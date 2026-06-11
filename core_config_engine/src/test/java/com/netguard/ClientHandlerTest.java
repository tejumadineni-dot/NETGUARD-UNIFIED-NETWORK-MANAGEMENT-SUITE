package com.netguard;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertNotNull;

/*
 * Unit Test Class for ClientHandler
 */
public class ClientHandlerTest {

    /*
     * Test Handler Object Creation
     */
    @Test
    public void testHandlerCreation() {

        // Create Handler Object
        ClientHandler handler =
                new ClientHandler(null);

        // Verify Object is Created
        assertNotNull(handler);
    }
}
