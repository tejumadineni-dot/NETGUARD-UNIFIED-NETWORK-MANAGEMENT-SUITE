package com.netguard;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

/*
 * Client Program
 * Sends firewall/VLAN update requests
 */
public class ConfigClient {

    public String sendMessage(String message) {

        try {

            Socket socket =
                    new Socket(
                            "localhost",
                            9090);

            PrintWriter writer =
                    new PrintWriter(
                            socket.getOutputStream(),
                            true);

            BufferedReader reader =
                    new BufferedReader(
                            new InputStreamReader(
                                    socket.getInputStream()));

            writer.println(message);

            String response =
                    reader.readLine();

            socket.close();

            return response;

        } catch (Exception e) {

            System.out.println(
                    "Client Error : "
                            + e.getMessage());

            return null;
        }
    }

    public static void main(String[] args) {

        ConfigClient client =
                new ConfigClient();

        String response =
                client.sendMessage(
                        "FIREWALL BULK UPDATE");

        System.out.println(
                "Server Response : "
                        + response);
    }
}