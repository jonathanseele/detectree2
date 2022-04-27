from setuptools import find_packages, setup

setup(
    name="src",
    version="0.0.1",
    author="James G. C. Ball",
    author_email="ball.jgc@gmail.com.com",
    description="Detectree packaging",
    url="https://github.com/PatBall1/detectree2",
    packages=find_packages(),
    test_suite="src.tests.test_all.suite",
    install_requires=[
        "pyyaml==5.1",
        "Cython",
        "cupy-cuda112",
        "cupy-cuda102",
        "torch",
        "torchvision",
        "torchaudio",
        "detectron2 @ git+https://github.com/facebookresearch/detectron2",
    ],
)
