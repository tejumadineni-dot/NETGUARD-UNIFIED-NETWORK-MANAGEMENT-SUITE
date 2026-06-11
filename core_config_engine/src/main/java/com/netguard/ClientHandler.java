package com.netguard;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

/*
 * Handles each client request
 * Runs in a separate thread
 */
public class ClientHandler implements Runnable {

    private Socket socket;

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {

        try {

            BufferedReader reader =
                    new BufferedReader(
                            new InputStreamReader(
                                    socket.getInputStream()));

            PrintWriter writer =
                    new PrintWriter(
                            socket.getOutputStream(),
                            true);

            String request = reader.readLine();

            System.out.println(
                    "Received Request : " + request);

            writer.println(
                    "Configuration Updated : " + request);

            socket.close();

        } catch (Exception e) {

            System.out.println(
                    "Client Handler Error : "
                            + e.getMessage());
        }
    }
}