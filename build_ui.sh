cp ejp_vocabulary_context.json docs
cp validation_vp_model/metadata_model.shex docs
jsonschema2md -e json -d . -n -o docs/ -x