package com.e_commerce_distribuido.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.e_commerce_distribuido.model.OrderModel;

@Repository
public interface OrderRepository extends JpaRepository<OrderModel, Long> {

    List<OrderModel> findByClientId(Long clientId);
}
