package com.netguard;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertNotNull;

/*
 * Unit Test Class for ConfigClient
 */
public class ConfigClientTest {

    /*
     * Test Client Object Creation
     */
    @Test
    public void testClientCreation() {

        // Create Client Object
        ConfigClient client =
                new ConfigClient();

        // Verify Object is Created
        assertNotNull(client);
    }
}