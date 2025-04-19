package com.e_commerce_distribuido.client_service.service;

import org.springframework.stereotype.Service;

import com.e_commerce_distribuido.client_service.dto.ClientRequestDTO;
import com.e_commerce_distribuido.client_service.mapper.ClientMapper;
import com.e_commerce_distribuido.client_service.repository.ClientRepository;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class ClientService implements IClientService{

    private final ClientRepository clientRepository;
    private final ClientMapper clientMapper;

    @Override
    public void createClient(ClientRequestDTO ClientRequestDTO) {
        clientRepository.save(clientMapper.toModel(ClientRequestDTO));
    }

}
