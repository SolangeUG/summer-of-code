'use strict';

class Dictionary {
    /**
     * Constructor: initialize a dictionary object from a text file
     * The root of our dictionary (implemented as a trie) is an empty string trie node.
     * @param dictFile: text file containing dictionary words
     */
    constructor(dictFile) {
        this.dictFile = dictFile;
        this.rootNode = new TrieNode("");
        this.searchMap = new Map();
        this.loadDictionary();
    }

    /**
     * Determine whether a given text string corresponds to a word in our dictionary
     * @param text: the text to be checked
     * @return {boolean} true if the string is in our dictionary, and false otherwise
     */
    isWord(text) {
        let exists = this.isPrefix(text);
        if (exists) {
            exists = false;
            let textNode = this.searchMap.get("endNode");
            if (textNode != null) {
                exists = textNode.endsWord;
            }
        }
        return exists;
    }

    /**
     * Determine whether a given text string corresponds to the prefix (of a word) in our dictionary
     * @param text: the text to be checked
     * @return {boolean} true if the string is a prefix of a word in our dictionary, and false otherwise
     */
    isPrefix(text) {
        if (! text) {
            return false;
        }
        // start exploring the trie from the root
        let current = this.rootNode;
        let exists = true;
        let upperText = text.toUpperCase();

        for (let i = 0; i < upperText.length; i++) {
            // for each character in our text, determine if exists corresponding node
            let char = upperText.charAt(i);
            let charNode = current.getChild(char);
            if (! charNode) {
                // if no node is found, then the input text is not in our dictionary
                exists = false;
                return exists;
            }
            current = charNode;
        }
        // at this point, each character of our input text has a corresponding node.
        // Therefore, the input text is definitely a prefix.

        // Use the searchMap to temporarily memorize the last search results.
        // That way, isWord can take advantage of isPrefix logic.
        this.searchMap.set("searchKey", text);
        this.searchMap.set("endNode", current);

        return true;
    }

    /**
     * Load a dictionary text file into our dictionary.
     * This dictionary is implemented as a trie.
     */
    loadDictionary() {

    }
}