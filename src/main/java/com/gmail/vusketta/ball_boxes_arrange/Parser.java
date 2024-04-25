package com.gmail.vusketta.ball_boxes_arrange;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.*;

public class Parser {
    private final Scanner reader;

    public Parser() {
        this(System.in);
    }

    public Parser(String fileName) throws FileNotFoundException {
        this(new FileInputStream(fileName));
    }

    public Parser(InputStream in) {
        this.reader = new Scanner(in);
    }

    public Map<String, Integer> parseSource() throws EOFException {
        skipLine(1); // skip Source data:

        final List<String[]> source = Arrays.stream(nextLine().split(", ")).map(it -> it.split(": ")).toList();
        final Map<String, Integer> parsed = new HashMap<>();
        source.forEach(it -> parsed.put(it[0], Integer.parseInt(it[1])));
        return parsed;
    }

    public List<Box> parseBoxes(final int boxNumber, final int colors) throws EOFException {
        List<Box> boxes = new ArrayList<>(boxNumber);
        for (int i = 0; i < boxNumber; i++) {
            boxes.add(i, parseBox(colors));
        }
        return boxes;
    }

    private Box parseBox(final int colors) throws EOFException {
        skip(4); // skip Box $number. Total: $number.

        final Map<String, Integer> balls = new HashMap<>();
        for (int i = 0; i < colors; i++) {
            final String color = next().replace(":", "");
            final int quantity = Integer.parseInt(next().replace(",", ""));
            balls.put(color, quantity);
        }
        return new Box(balls);
    }

    public List<Experiment> parseExperiments(final int experimentsNumber, final int arrangements) throws EOFException {
        final List<Experiment> experiments = new ArrayList<>(experimentsNumber);
        skipLine(2); // Experiments: & previous line
        for (int i = 0; i < experimentsNumber; i++) {
            experiments.add(i, parseExperiment(arrangements));
        }
        return experiments;
    }

    private Experiment parseExperiment(final int arrangements) throws EOFException {
        skip(3); // skip # 1, Balls:
        return new Experiment(Arrays.stream(nextLine().trim().split(", ")).toList().subList(0, arrangements));
    }

    private String next() throws EOFException {
        if (reader.hasNext()) return reader.next();
        throw new EOFException();
    }

    private String nextLine() throws EOFException {
        if (reader.hasNextLine()) return reader.nextLine();
        throw new EOFException();
    }

    private void skipLine(int number) {
        for (int i = 0; i < number; i++) {
            reader.nextLine();
        }
    }

    private void skip(int number) {
        for (int i = 0; i < number; i++) {
            reader.next();
        }
    }
}
