package com.e_commerce_distribuido.client_service.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.e_commerce_distribuido.client_service.dto.ClientRequestDTO;
import com.e_commerce_distribuido.client_service.dto.ClientResponseDTO;
import com.e_commerce_distribuido.client_service.service.IClientService;

import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;


@RestController
@RequestMapping("/api/v1/clients")
@RequiredArgsConstructor
public class ClientController {
    
    private final IClientService clientService;

    @PostMapping
    public ResponseEntity<String> createClient(@RequestBody ClientRequestDTO clientRequestDTO) {
        clientService.createClient(clientRequestDTO);
        return ResponseEntity.ok("Client created successfully");
    }

    @GetMapping("/{clientId}")
    public ResponseEntity<ClientResponseDTO> getClientById(@PathVariable Long clientId) {
        clientService.getClientById(clientId);
        return ResponseEntity.ok(clientService.getClientById(clientId));
    }
    
}
