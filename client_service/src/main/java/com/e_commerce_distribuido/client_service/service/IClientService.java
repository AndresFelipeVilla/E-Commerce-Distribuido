package com.e_commerce_distribuido.client_service.service;

import com.e_commerce_distribuido.client_service.dto.ClientRequestDTO;
import com.e_commerce_distribuido.client_service.dto.ClientResponseDTO;

public interface IClientService{
    void createClient(ClientRequestDTO ClientRequestDTO);
    ClientResponseDTO getClientById(Long id);
}
