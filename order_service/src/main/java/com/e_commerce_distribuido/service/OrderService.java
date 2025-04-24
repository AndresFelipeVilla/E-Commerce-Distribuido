package com.e_commerce_distribuido.service;

import java.util.List;

import org.springframework.http.HttpStatusCode;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;

import com.e_commerce_distribuido.dto.ClientResponseDTO;
import com.e_commerce_distribuido.dto.OrderRequestDTO;
import com.e_commerce_distribuido.dto.OrderResponseDTO;
import com.e_commerce_distribuido.exception.OrderNotFoundException;
import com.e_commerce_distribuido.mapper.OrderMapper;
import com.e_commerce_distribuido.model.OrderModel;
import com.e_commerce_distribuido.repository.OrderRepository;

import lombok.RequiredArgsConstructor;
import reactor.core.publisher.Mono;

@Service
@RequiredArgsConstructor
public class OrderService implements IOrderService {

    private final OrderRepository orderRepository;
    private final OrderMapper orderMapper;
    private final WebClient webClient;


    @Override
    public void createOrder(OrderRequestDTO orderRequest) {
        ClientResponseDTO client = getClientById(orderRequest.clientId());
        if (client == null) {
            throw new RuntimeException("Client not found");
        }

        OrderModel order = orderMapper.toEntity(orderRequest);
        order.setCustomerName(client.getName());
        orderRepository.save(order);
    }


    @Override
    public OrderResponseDTO getOrderById(Long orderId) {
        OrderModel order = orderRepository.findById(orderId)
        .orElseThrow(() -> new OrderNotFoundException(orderId)); 
        return orderMapper.toDTO(order);
    }


    @Override
    public List<OrderResponseDTO> getAllOrdersByClientId(Long clientId) {
        List<OrderModel> orders = orderRepository.findByClientId(clientId);
        return orders.stream()
                .map(orderMapper::toDTO)
                .toList();
    }


    @Override
    public void deleteOrder(Long orderId) {
        if (!orderRepository.existsById(orderId)) {
            throw new OrderNotFoundException(orderId);
        }
        orderRepository.deleteById(orderId);
    }

    private ClientResponseDTO getClientById(Long clientId) {
        return webClient.get()
            .uri("/clientes/{id}", clientId)  
            .retrieve()
            .onStatus(HttpStatusCode::is4xxClientError, response -> {
                return Mono.error(new RuntimeException("Client not found"));
            })
            .bodyToMono(ClientResponseDTO.class)
            .block();   
    }

}
