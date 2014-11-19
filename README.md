# Nose Git Tests - Only run tests tracked by Git

I often create files named test.py or something in the root of a project for
playing around.  Unfortunately, nosetests picks these up and runs them, leading
me to wasted seconds of confusion when I discover that the test suite isn't actually
failing.  This nose plugin will require that a file be tracked in Git before being
run by nosetests.

# TODO

  - Properly handle scenario when we're not in a Git repository
