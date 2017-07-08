================================
History of North Sea Discoveries
================================

The history of the North Sea, using d3.

Does the visualisation have a clear finding?

Does it focus on it's finding?

Getting started
---------------

Clone the repository

Use python to create a local server (or any other tool).

::

    $ python -m http.server

Then open up a localhost on port 8000 (default for python) in your browser.

    http://localhost:8000/.../North_Sea_Visualisation/


Design Approach
---------------

Following exploratory data analysis of the North Sea NPD dataset
the approach is to create an author driven narrative.

The author driven narrative  will demonstrate that overtime the amount of hydrocarbons have decreased which will affect the future of Norway.


Initial design decisions
------------------------

The initial design choice is a buble chart.

The chart can use production per year against each field (categorical values).
Visual encodings will be position with year along the x axis and production in oil equivalents on the y axis.

The size of the bubble can be taken by an additional variable for example total oil to show the difference between oil and gas.


Visualisation development process
---------------------------------

Some attempts were made using dimple.js and raw.io. This was a useful experience to shape the design process.


Bubble chart v1
^^^^^^^^^^^^^^^

Based on the initial design decision a bubble chart was created.

.. figure:: resources\images\Bubble_chart_v1.png
   :scale: 100 %

   Bubble chart of production per year for each fiel, created using rawgraphs.io


There are a number of issues with this graph. There are too many categories obscuring the image, especially in the lower values.

The magnitude of values between small and large makes it challenging to see any information in the smaller values.

It does not effectively draw attention to any changes in time apart from highlighting changes in a few key cateogires poorly.


Steam chart v1
^^^^^^^^^^^^^^

After reviewing Andy Kirk´s book, Data Visualisation one option that jumped out for this case is the stream graph.

This addresses the complication of the magnitude of difference between categorical groups.

It also fits nicely as there is a certain ebb & flow to this data over time that will help communicate the narrative.

http://www.visualisingdata.com/2010/08/making-sense-of-streamgraphs/

.. figure:: resources\images\Stream_Chart_v1.png
   :scale: 100 %

   Stream graph production per year for each fiel, created using rawgraphs.io



Feedback
--------




Data
----

Datasets are from the NPD (Norwegian Petroleum Directorate) stored on data.norge (

http://data.norge.no/data/oljedirektoratet/felt-field

Data is stored under the Norwegian Licence for Open Government Data (NLOD)

http://data.norge.no/nlod/en

http://data.norge.no/nlod/en/1.0


Work Process
------------


Wrap-up
-------



Resources
---------

`Google JavaScript Style Guide <https://google.github.io/styleguide/jsguide.html>`_

