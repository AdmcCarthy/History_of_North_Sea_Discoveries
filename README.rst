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


Steam graph v1
^^^^^^^^^^^^^^

After reviewing Andy Kirk´s book, Data Visualisation one option that jumped out for this case is the stream graph.

This addresses the complication of the magnitude of difference between categorical groups.

It also fits nicely as there is a certain ebb & flow to this data over time that will help communicate the narrative.

http://www.visualisingdata.com/2010/08/making-sense-of-streamgraphs/

.. figure:: resources\images\Stream_Chart_v1.png
   :scale: 100 %

   Stream graph production per year for each field, created using rawgraphs.io

The figure is still quite distracting.

The colours are distracting and do not seperate the categories easily, there are too many labels which do not help convey a narrative.

There is a steep decrease (a decline in total production) at the end of the chart, this is not highlighted cleary enough.

Other technical issues include the years being incorrectly displayed.


Stream graph v2
^^^^^^^^^^^^^^^

After reviewing the last attempt the narrative was not being delivered. Although this showed
alterations in production as a rate per year it did not communicate total changes over time. It did not communicate a change
in the History of the North Sea adequately.

Some data processing was undertaken to create a new variable. Each fields reserves were taken and then the production per
year was subtracted cumalatively. The idea being this would communicate changes over time by showing a decrease of the original total.

.. figure:: resources\images\Stream_graph_v2.png
   :scale: 100 %

   Stream graph reserves remaining per year for each field, created using rawgraphs.io

The result is a better vehicle to deliver the narrative of the history of the North Sea.

This will now be taken into d3.js as this is the only way to get proper control on colour, labels, annotations
and other features.

Labels and categorical colors will be a challenge. It will likely be best to think of a way to limit
the color range and labels to make it more digestable.

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

