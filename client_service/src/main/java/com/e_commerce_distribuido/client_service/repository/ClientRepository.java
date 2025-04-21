package com.e_commerce_distribuido.client_service.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.e_commerce_distribuido.client_service.model.ClientModel;

@Repository
public interface ClientRepository extends JpaRepository<ClientModel, Long> {
    
} 
