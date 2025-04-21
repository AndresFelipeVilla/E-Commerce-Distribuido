package com.e_commerce_distribuido.client_service.mapper;

import org.springframework.stereotype.Component;

import com.e_commerce_distribuido.client_service.dto.ClientRequestDTO;
import com.e_commerce_distribuido.client_service.model.ClientModel;

@Component
public class ClientMapper {

    public ClientModel toModel(ClientRequestDTO clientRequestDTO) {
        return ClientModel.builder()
                .name(clientRequestDTO.getName())
                .email(clientRequestDTO.getEmail())
                .password(clientRequestDTO.getPassword())
                .address(clientRequestDTO.getAddress())
                .phoneNumber(clientRequestDTO.getPhoneNumber())
                .build();
    }
}
