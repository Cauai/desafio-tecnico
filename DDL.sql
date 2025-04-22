CREATE TABLE sales (
    order_number BIGINT PRIMARY KEY,
    total_value NUMERIC(12,2) NOT NULL,
    processed_at TIMESTAMP NOT NULL
);