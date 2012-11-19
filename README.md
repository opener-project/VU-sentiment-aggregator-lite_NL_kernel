# Opener::Kernel::VU::Sentiment-Aggregator::lite::NL

## Initial Version

VU-sentiment-aggregator-lite_NL
===============================

Sentiment-aggregator for Dutch Lite versionVU-polarity-tagger-lite_NL

This module implements a sentiment aggregator based on a set of predefined rules considering polarity
shifters and intensifiers. The program reads from the
standard input and writes the output in the standard output. The most simple way to run
the program is:

````shell
$ cat myfile.kaf | ./core/sentimentAggregatorLite.py > myfile.out.kaf
````

Use the option --no-time if you want to exclude the timestamp information in the linguisticProccesors
information (for testing purposes)


The input has to be a KAF valid file with at least the term layer including
sentiment at the term level. The output will be a KAF file with the opinion
layer created (or extendend) with the overall opinion computed over the basic polarities
of the terms and with the application of a set of rules.


Install the Requirements
-----------------------

The VU-sentiment-aggregator-lite_NL relies on some external dependencies. Which are described inthe requirement.txt file.
An easy way to manage the dependencies, given that you use a unix/mac oriented machine, is to follow the installation of [virtualenv_burrito](https://github.com/brainsik/virtualenv-burrito).

After you've installed virtualenv_burrito create a "virtual python environment" using

````shell
mkvirtualenv opener
````

Now go to the directory of this repository and type

````shell
pip install -r requirements.txt
````

To install all the dependencies of the VU-sentiment-aggregator-lite_NL


Combining things
----------------

It is also possible to combine the two kernels for dutch: the tokenizer and the polarity tagger, using for instance
a shell pipeline.

````shell
$ cat my_plain_text |
  $PATHtokenizer/SimpleTokenizer.py |
  $PATHpol-tagger/SimplePolarityTagger.py |
  $PATHsent-aggregator/SentimentAggregatorLite.py.py
  > my_file.kaf                  
````

Later on a tested "configuration" approach will be provided.

## Installation

Add this line to your application's Gemfile:

    gem 'VU-sentiment-aggregator-lite_NL', :git=>"git@github.com/opener-project/VU-sentiment-aggregator-lite_NL.git"

And then execute:

    $ bundle install

Or install it yourself as:

    $ gem install VU-sentiment-aggregator-lite_NL -l https://github.com/opener-project/VU-sentiment-aggregator-lite_NL.git

## Usage

Once installed as a gem you can access the gem from anywhere:


TODO: Change output below as needed
````shell
echo "foo" | VU-sentiment-aggregator-lite_NL 
````

Will output

````
oof
````

## Contributing

1. Pull it
2. Create your feature branch (`git checkout -b features/my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin features/my-new-feature`)
5. If you're confident, merge your changes into master.
