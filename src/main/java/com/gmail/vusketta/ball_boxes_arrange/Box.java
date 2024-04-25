package com.gmail.vusketta.ball_boxes_arrange;

import java.util.Map;

public record Box(Map<String, Integer> balls) {
    public int total() {
        return balls.values().stream().reduce(0, Integer::sum);
    }

    @Override
    public String toString() {
        return "Box(Total: " + total() + ". " + balls + ')';
    }
}
