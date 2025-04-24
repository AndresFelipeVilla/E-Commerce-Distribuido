package com.e_commerce_distribuido.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class OrderResponseDTO {
    private Long id;
    private Long clientId;
    private String customerName;
    private String productName;
    private int quantity;
    private double price;
}
