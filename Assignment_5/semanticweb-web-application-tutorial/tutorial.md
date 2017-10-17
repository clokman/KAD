## 5. The **Semantic Web** Tutorial

Once you have Python, Java and Stardog in place, you can try out the Semantic Web tutorial.

* Open up a Terminal or a Command Prompt window
* Change directory to e.g. your Documents directory (on Mac/Linux: `cd ~/Documents`, on Windows `cd C:\Users\YOURUSERNAME\Documents`)
* If you have GIT, you can "clone" the source code from Github. Type: `git clone https://github.com/kadevgraaf/semanticweb-web-application-tutorial.git web-application` to clone it into a folder called `web-application`
* Otherwise, download the zip file from <https://github.com/kadevgraaf/semanticweb-web-application-tutorial/archive/master.zip> and unzip to a folder called `web-application`
* Change directory to the newly created folder: `cd web-application`
* (**OPTIONAL**) Setup the virtualenv in the directory of this repository (`virtualenv .`)
* (**OPTIONAL**) Activate the virtualenv (`source bin/activate` on linux-like systems)
* Install the necessary packages (`pip install -r requirements.txt`)
* Check the Stardog SPARQL endpoint URL in the `TUTORIAL_REPOSITORY` variable in **both** `src/tutorial.py` and `src/static/js/tutorial.js`.  
* If you haven't done so, install **Stardog** and make sure it is running.
  * By default, the script assumes a Stardog database with the name 'tutorial' running at <http://localhost:5820/tutorial>.
  * The database should have `reasoning set to `SL` and "SameAs reasoning" to `FULL`.
	* Start your Stardog server with `stardog-admin server start --disable-security` (don't forget the `--disable-security` flag!). To stop Stardog, run `stardog-admin server stop`.
	* If you want to use a different name or location (i.e. not running on localhost, port 5820) you need to set the `TUTORIAL_REPOSITORY` variable in `src/tutorial.py`, and make appropriate modifications to the Stardog configuration.
* Run the tutorial from within the `src` directory by running `python tutorial.py`

Other information on how to run the tutorial can be found in the readme file on the GitHub page of the tutorial: <https://github.com/kadevgraaf/semantic-web-application-tutorial>.

#### The Ultimate Test: does it work?

Go to <http://localhost:5000> in your browser.

* In step 10,
  * type `Aspirin`, (this retrieves all matches for Aspirin from Linked Life Data)
  * select the link `Aspirin`,
  * and press the "Link" button. This pushes the RDF representation of LLD Aspirin to your Stardog instance.
  * Output should be 'Ok!'
* In step 11,
  * also type `Aspirin` (this will retrieve all matches for Aspirin from DBPedia),
  * select the link `Aspirin`,
  * and press the "Link" button.
  * Output should be 'Ok!'
* In step 12,
  * just press the "Link" button.
  * Output should be 'Ok!'
* Skip step 13
* In step 14,
   * just press the "Link" button.
   * Output should have two results, one from Linked Life Data, and one from DBPedia.
