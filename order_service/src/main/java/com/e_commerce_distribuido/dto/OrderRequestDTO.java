package com.e_commerce_distribuido.dto;

public record OrderRequestDTO(
        String customerName,
        String productName,
        int quantity,
        Long clientId,
        Double price) {
} 