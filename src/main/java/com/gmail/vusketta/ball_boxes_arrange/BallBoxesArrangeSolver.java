package com.gmail.vusketta.ball_boxes_arrange;

import com.gmail.vusketta.utils.Solver;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.List;
import java.util.Map;

public class BallBoxesArrangeSolver implements Solver {
    private final InputStream in;

    public BallBoxesArrangeSolver() {
        this.in = System.in;
    }

    public BallBoxesArrangeSolver(String fileName) throws FileNotFoundException {
        this.in = new FileInputStream(fileName);
    }

    public BallBoxesArrangeSolver(InputStream in) {
        this.in = in;
    }

    @Override
    public void solve() throws EOFException {
        final Parser parser = new Parser(in);
        final Map<String, Integer> source = parser.parseSource();
        final List<Box> boxes = parser.parseBoxes(source.get("n_boxes"), source.get("m"));
        final List<Experiment> experiments = parser.parseExperiments(source.get("nExp"), source.get("d"));

        boxes.forEach(System.out::println);
        experiments.forEach(System.out::println);
    }
}
