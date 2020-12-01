cp ejp_vocabulary_context.json docs
cp validation_vp_model/metadata_model.shex docs
jsonschema2md -p example -e json -d json_schema/ -n -o docs/
git add docs/*.md
git add docs/*.json
