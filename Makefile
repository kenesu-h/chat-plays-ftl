all: chat-plays-ftl clean

chat-plays-ftl: .FORCE
	./bin/win-pyinstaller/bin/pyinstaller.exe src/main.py -n chat-plays-ftl -F
	chmod u+x dist/chat-plays-ftl
	mv dist/chat-plays-ftl ./chat-plays-ftl

clean:
	rm -f chat-plays-ftl.spec
	rm -r -f build
	rm -r -f dist

.FORCE: