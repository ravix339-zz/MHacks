# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Example code for TensorFlow Wide & Deep Tutorial using TF.Learn API."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import tempfile

import pandas as pd
from six.moves import urllib
import tensorflow as tf

training_file = 'C:\\Users\\Ravi\\Desktop\\idk.csv'
testing_file = 'C:\\Users\\Ravi\\Desktop\\idk.csv'
CSV_COLUMNS = ["sentiment", "delta_price"]

# Continuous base columns.
sentiment = tf.feature_column.numeric_column("sentiment")

base_columns = [sentiment]


def build_estimator(model_dir):
    """Build an estimator."""
    m = tf.estimator.DNNLinearCombinedRegressor(
        model_dir=model_dir, linear_feature_columns=base_columns,
        dnn_feature_columns=base_columns, dnn_hidden_units=[100, 50])
    return m


def input_fn(data_file, num_epochs, shuffle):
    """Input builder function."""
    df_data = pd.read_csv(
        tf.gfile.Open(data_file),
        names=CSV_COLUMNS,
        skipinitialspace=True,
        engine="python",
        skiprows=1)
    # remove NaN elements
    df_data = df_data.dropna(how="any", axis=0)
    known_deltas = df_data["delta_price"]
    return tf.estimator.inputs.pandas_input_fn(
        x=df_data,
        y=known_deltas,
        batch_size=100,
        num_epochs=num_epochs,
        shuffle=shuffle,
        num_threads=5)


def train_and_eval(model_dir, train_steps):
    """Train and evaluate the model."""
    model_dir = tempfile.mkdtemp() if not model_dir else model_dir

    m = build_estimator(model_dir)
    # set num_epochs to None to get infinite stream of data.
    m.train(
        input_fn=input_fn(training_file, num_epochs=None, shuffle=True),
        steps=train_steps)
    # set steps to None to run evaluation until all data consumed.
    results = m.evaluate(
        input_fn=input_fn(testing_file, num_epochs=1, shuffle=False),
        steps=None)
    print("model directory = %s" % model_dir)
    for key in sorted(results):
        print("%s: %s" % (key, results[key]))

    predictions = m.predict(input_fn=input_fn(testing_file, num_epochs=1, shuffle=False))
    for i, p in enumerate(predictions):
        if i == 0:
            print("Prediction %s: %s" % (225, p))
        elif i == 1:
            print("Prediction %s: %s" % (400, p))
        elif i == 2:
            print("Prediction %s: %s" % (1089, p))


FLAGS = None


def main(_):
    train_and_eval(FLAGS.model_dir, FLAGS.train_steps)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.register("type", "bool", lambda v: v.lower() == "true")
    parser.add_argument(
        "--model_dir",
        type=str,
        default="",
        help="Base directory for output models."
    )
    parser.add_argument(
        "--train_steps",
        type=int,
        default=2000,
        help="Number of training steps."
    )
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
