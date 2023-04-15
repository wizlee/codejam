## Overview
The last CodeJam creates a big enough motivation for me to join despite the awkward timezone.

GL HF! 

## Final Thought after participating
> This has been a fun one 😎

- Have the most fun attempting problem 2 `Illumination Optimisation`
- Running short on time as joining an hour late. 
    - Still, with this experience learnt how to analyse a problem better
    - better equiped with common coding patterns to solve problem faster
- Randomly view a few people that got 100% and noticed that they are all using C++
    - C++ does have an advantage in precise memory management and more performant. 
    - However I wonder
        - If this happens partially due to people with C++ skills usually are better with algorithm
        - If I will be able to do better if I chose C++ instead of Python.
            - I doubt I will do better unless I invest significant amount of time practicing.
            - Python has a lot of nice shorthand and even though I am familar with C++ I don't have any experience of using it to solve problem quickly in a time-boxed manner.
- ==Learnings==
    - `[[]] * 5` and `[[] for _ in range(5)]` defers in that the first approach results in a nested list where all the inner list references the SAME list.
    - Practise and preparation really helps a lot in time-boxed coding challenge.
        - Despite only prepare a rough template that helps with getting inputs into data structures, that already helps speed up significantly.
        - Only after a round of competition, my template is already much better that before I started.
        - Will look for other coding competition to join so that my templates don't go to waste! 🤘



## Motivation
- Aside from the rarity of this will be the final round, the main purpose of joining are to improve my programming skills and add experiences in my portfolio.
- In my opinion, a great competitor in coding competition such as CodeJam will not gurantee a great programmer.
    - The main reason being a great programmer must also write clean code and able to communicate well among other things.
    - However, being a great competitor will certainly means a better problem solving ability and better in using algorithm. This is certainly an critical part of being a good programmer. 

## Useful Details for 2023 Farewell Round
- All info are from the [FAQ](https://codingcompetitions.withgoogle.com/codejam/faq) and [Rules](https://codingcompetitions.withgoogle.com/codejam/rulesandterms) page.
- Contrast to previous years, there will not be next round. This farewell round is the only round.
- There are 4 rounds within the Farewell round
    - All rounds starts and ends at the same time.
    - There is no limit on how many round one person can join.
    - No prize for any rounds this time.
- Difficulty of each round
    - Round A is appropriate for beginners.
    - Round B is about the level of a Kick Start round or a Code Jam Round 1.
    - Round C is harder than a Code Jam Round 2 but easier than a Code Jam Round 3.
    - Round D is meant for experienced competitors. It is between a Code Jam Round 3 and Finals difficulty.
- Some problem might only be possible to solve by using C++ due to performance reason.

## CodeJam Platform Specifications
- https://codingcompetitions.withgoogle.com/codejam/faq#platform
- 64-bit version of Debian 10.9 (buster)
    - Install package using `apt-get install -y --no-install-recommends <package>`
- Linux Kernel
    - Linux version 4.19.0-16-cloud-amd64
    - package: linux-image-cloud-amd64
- Stack size limit
    - 64 MB per language, defined by `ulimit -s 65536`
    - JVM-based languages are passed the `-Xss64m` flag during execution.
- Languages Specific specs
    - C++
        - gcc 8.3.0 (packages: gcc, g++)
        - `g++ Solution.cc -std=c++17 -pthread -O2 -o Solution`
        - ./Solution
    - Python 3:
        - 3.7.3 (package: python3.7)
            - numpy 1.19.3 (`pip install numpy`)
            - scipy 1.5.3 (`pip install scipy`)
        - python3 Solution.py

## Interactive Problem
- In an interactive problem, our judging system and your code run at the same time.
- When you send output to your output stream, the judge reads that output and then responds by sending input to your input stream. 
    - Then your code reads that input, and determines what output to send next, and so on. Each test set proceeds in this way.
    - Generally, the judge tells your code when a test set has been solved, or when you have failed the test set.
- Must flush your output buffer every time output data to the judge
    - Else the judge might end up waiting forever for output that never comes
    - Refer to the templates for cpp and python respectively for sample to flush output
- Others
    - stderr is ignored but need to take care to not overflow it to not affect memory limit
    - Should not send any additional output after processing all test cases. Will result in 'Wrong Answer' judgement if do otherwise.
    - To test solution locally, use CodeJam [interactive_runner.py script](https://storage.googleapis.com/coding-competitions.appspot.com/interactive_runner.py) in conjunction with the judge.
        - The judge will be included at the bottom of an interactive problem statement. 
