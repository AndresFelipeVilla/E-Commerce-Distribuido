package com.e_commerce_distribuido.service;

import java.util.List;

import com.e_commerce_distribuido.dto.OrderRequestDTO;
import com.e_commerce_distribuido.dto.OrderResponseDTO;

public interface IOrderService {
    void createOrder(OrderRequestDTO orderRequest);
    OrderResponseDTO getOrderById(Long orderId);
    List<OrderResponseDTO> getAllOrdersByClientId(Long clientId);
    void deleteOrder(Long orderId);
    
}
