package com.e_commerce_distribuido.client_service.dto;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class ClientResponseDTO {
    private String name;
    private String email;
    
}
