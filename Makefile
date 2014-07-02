build: clean
	@mkdir -p ./build
	@for file in ./slides/*; do cat $$file >> ./build/slides.md; echo '\r\n---\r\n' >> ./build/slides.md; done;
	@gsed -i -e :a -e '$$d;N;2,3ba' -e 'P;D' ./build/slides.md
	@cp ./template.html ./build/index.html
	@gsed -i -e "/{{slides}}/r ./build/slides.md" -e "//d" ./build/index.html

clean:
	@rm -rf ./build

run: build
	@cd ./build && python -m SimpleHTTPServer

.PHONY: build clean run
