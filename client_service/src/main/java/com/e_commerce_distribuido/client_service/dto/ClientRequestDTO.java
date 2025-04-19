package com.e_commerce_distribuido.client_service.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class ClientRequestDTO {
    private String name;
    private String email;
    private String password;
    private String address;
    private String phoneNumber;
}
