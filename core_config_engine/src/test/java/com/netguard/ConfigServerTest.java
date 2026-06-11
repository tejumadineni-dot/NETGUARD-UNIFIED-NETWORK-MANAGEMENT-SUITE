package com.netguard;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertNotNull;

/*
 * Unit Test Class for ConfigServer
 */
public class ConfigServerTest {

    /*
     * Test Server Object Creation
     */
    @Test
    public void testServerCreation() {

        // Create Server Object
        ConfigServer server =
                new ConfigServer();

        // Verify Object is Created
        assertNotNull(server);
    }
}
