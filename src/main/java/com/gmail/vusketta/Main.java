package com.gmail.vusketta;

import com.gmail.vusketta.ball_boxes_arrange.BallBoxesArrangeSolver;

import java.io.EOFException;
import java.io.FileNotFoundException;

public class Main {
    public static void main(String[] args) throws EOFException, FileNotFoundException {
        System.out.println("Hello world!");

        BallBoxesArrangeSolver solver = new BallBoxesArrangeSolver(
                "src/main/resources/task_1_ball_boxes_arrange.txt"
        );

        solver.solve();
    }
}