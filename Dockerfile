# We first build the stork-search binary from 
# the source code and then we add it to the
# pandoc/latex image
FROM rust:alpine as builder

# We install cryptographic and devel
# libraries needed for the build
# Note: these will be statically linked
# hence we do not need to copy them to
# the next stage
RUN apk add --no-cache  \
    musl-dev            \
    pkgconfig           \  
    libc-dev            \
    openssl-dev         \
    openssl-libs-static \
    build-base

# Then we install the stork-search binary
RUN cargo install     \
          --root /bin \
          stork-search --locked

# We use pandoc/latex as a base
# it is an alpine distribution too
FROM pandoc/latex

# Copy the binary form previous stage
# due to a typo in the previous command
# the executable in in /bin/bin/stork
COPY --from=builder /bin/bin/stork /bin/stork

# Install the texlive packages needed
# for the build
# - knowledge
# - currfile
# - tikz-cd
# - tikz
# we reinstall biber so that it is
# using the same version as the
# biblatex package in the texlive distribution
RUN tlmgr update --self
RUN tlmgr update     \
          knowledge  \
          currfile   \
          biber      \
          tikz-cd    

# we add to pandoc/latex
# the following binary packages
# - make
# - inkscape
# - git
# - websocat
# - pandoc
# - python3 / pip3
#   - panflute (python package)
#   - dateparser (python package)
#   - icalendar (python package)
# - entr
# - wget (to get stork-search)
# - zip
# - tar (gnutar)

RUN apk add --no-cache \
    inkscape           \
    make               \
    git                \
    entr               \
    zip                \
    websocat           \
    wget               \
    tar

# Install the python3 libraries needed
RUN apk add --no-cache \
        python3        \
        py3-pip

RUN pip3 install --break-system-packages \
         panflute                        \
         dateparser                      \
         icalendar
