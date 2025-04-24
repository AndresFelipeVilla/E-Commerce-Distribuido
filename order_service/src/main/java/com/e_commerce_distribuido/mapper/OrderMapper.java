package com.e_commerce_distribuido.mapper;

import org.springframework.stereotype.Component;

import com.e_commerce_distribuido.dto.OrderRequestDTO;
import com.e_commerce_distribuido.dto.OrderResponseDTO;
import com.e_commerce_distribuido.model.OrderModel;


@Component
public class OrderMapper {

    public OrderModel toEntity(OrderRequestDTO orderDTO) {
        return OrderModel.builder()
                .customerName(orderDTO.customerName())
                .productName(orderDTO.productName())
                .quantity(orderDTO.quantity())
                .clientId(orderDTO.clientId())
                .price(orderDTO.price())
                .build();
    }

    public OrderResponseDTO toDTO(OrderModel order) {
        return OrderResponseDTO.builder()
                .id(order.getId())
                .customerName(order.getCustomerName())
                .productName(order.getProductName())
                .quantity(order.getQuantity())
                .clientId(order.getClientId())
                .price(order.getPrice())
                .build();
    }
}    
