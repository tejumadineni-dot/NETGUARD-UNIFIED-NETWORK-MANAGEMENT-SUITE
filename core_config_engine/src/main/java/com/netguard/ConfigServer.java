package com.netguard;

import java.net.ServerSocket;
import java.net.Socket;

public class ConfigServer {

    private static final int PORT = 9090;

    public void startServer() {

        try (ServerSocket serverSocket =
                     new ServerSocket(PORT)) {

            System.out.println(
                    "NetGuard Config Server Started on Port "
                            + PORT);

            while (true) {

                Socket socket =
                        serverSocket.accept();

                System.out.println(
                        "Client Connected");

                Thread thread =
                        new Thread(
                                new ClientHandler(socket));

                thread.start();
            }

        } catch (Exception e) {

            System.out.println(
                    "Server Error : "
                            + e.getMessage());
        }
    }

    public static void main(String[] args) {

        ConfigServer server =
                new ConfigServer();

        server.startServer();
    }
}