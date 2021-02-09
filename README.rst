pl-CT-covidnet
================================

.. image:: https://img.shields.io/github/license/FNNDSC/pl-CT-covidnet
    :target: https://github.com/FNNDSC/pl-CT-covidnet/blob/master/LICENSE
    :alt: License AGPL-3.0

.. image:: https://img.shields.io/docker/v/fnndsc/pl-ct-covidnet?sort=semver
    :target: https://hub.docker.com/r/fnndsc/pl-ct-covidnet


.. contents:: Table of Contents


Abstract
--------

``ct_covidnet.py`` is a ChRIS-based plugin for the COVIDNet-UI that performs classification of COVID-19 from chest CT images.
More details on the implementation can be found on the paper,
`COVIDNet-CT: A Tailored Deep Convolutional Neural Network Design for Detection of COVID-19 Cases from Chest CT Images <https://arxiv.org/abs/2009.05383>`_.

Arguments
---------

.. code::

    [--imagefile]
    required, name of the image file to be analyzed 


Local Build
-----------

.. code:: bash

    DOCKER_BUILDKIT=1 docker build -t local/pl-ct-covidnet .


Run
----

.. code:: bash

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing  \
            fnndsc/pl-ct-covidnet:0.2.0a1 ct_covidnet               \
            --imagefile ex-covid-ct.png                             \
            /incoming /outgoing


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
