package com.gmail.vusketta.ball_boxes_arrange;

import java.util.List;

public record Experiment(List<String> balls) {
    @Override
    public String toString() {
        return "Balls: " + balls;
    }
}
