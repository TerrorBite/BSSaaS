# BSSaaS
Broad Sweeping Statements as a Service

0.1.1

[![Build Status](https://travis-ci.org/zenoio/BSSaaS.svg?branch=master)](https://travis-ci.org/zenoio/BSSaaS)

BSSaaS (Broad Sweeping Statements as a Service) provides a modern, RESTful, scalable solution to the common problem of needing a broad sweeping statement.

Please see http://bssaas.com for API documentation and examples.

# Installation

	npm install

# Run

	npm start

# Test

	npm test


# Integrate BSSaaS

# Contributing

## Adding new operations

To add a new BSSaaS operation:

1. Fork into your account
2. Branch into a feature branch `feature/your_operation`
3. See the operation files in `/lib/operations`.
4. Add specs, using `/spec/operations` as examples. We won't be merging operations without working specs.
5. Push to your fork and submit a PR.

For the time being, in your PR, please include relevant documentation in `public/index.html`.

All contributions are very welcome.
