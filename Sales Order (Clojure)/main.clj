(defn parse-float [x]
  (.parse (java.text.NumberFormat/getInstance) x)
)
(defn parse-int [s]
   (Integer. (re-find  #"\d+" s ))
)

(defn print-menu []
  (println "\n\n" "*** Sales Menu ***")
  (println "------------------")
  (println "1. Display Customer Table\n2. Display Product Table\n3. Display Sales Table\n4. Total Sales for Customer\n5. Total Count for Product\n6. Exit")
  (println "\nEnter an option?")
)
(defn option-1 [t_list]
  (def size (count t_list))
  (loop [i 0]
    (when (< i size)
      (def cust-temp (get t_list i))
      (loop [j 0]
        (when (< j (count cust-temp))
          (if (= j 0) (print (get cust-temp j)":" "[") (print "\"" (get cust-temp j) "\""))
          (if (> j 2) (println "]"))
          (recur (+ j 1))
        )
      )
      (recur (+ i 1))
    )
  )
)
(defn option-2 [t_list]
  (def size (count t_list))
  (loop [i 0]
    (when (< i size)
      (def cust-temp (get t_list i))
      (loop [j 0]
        (when (< j (count cust-temp))
          (if (= j 0) (print (get cust-temp j)":" "[") (print "\"" (get cust-temp j) "\""))
          (if (> j 1) (println "]"))
          (recur (+ j 1))
        )
      )
      (recur (+ i 1))
    )
  )
)
(defn option-3 [cust-list prod-list sales-list]
  (loop [i 0]
    (when (< i (count sales-list))
      (def temp-sale (get sales-list i))
      (print (get temp-sale 0) ":")
      (loop [j 0]
        (when (< j (count cust-list))
          (if (= (get temp-sale 1) (get (get cust-list j) 0)) (print "[\"" (get (get cust-list j) 1) "\""))
          (recur (+ j 1))
        )
      )
      (loop [k 0]
        (when (< k (count prod-list))
          (if (= (get temp-sale 2) (get (get prod-list k) 0)) (print "\"" (get (get prod-list k) 1) "\""))
          (recur (+ k 1))
        )
      )
      (println "\""(get temp-sale 3) "\"]")
      (recur (+ i 1))
    )
  )
)
(defn option-4 [cust-list prod-list sales-list]
  (println "Customer Name: ")
  (def input (read-line))
  (def cust-id "")
  #_(def temp-vec [])
  (def total 0.0)
  (loop [i 0]
    (when (< i (count cust-list))
      (if (= (compare input (get (get cust-list i) 1)) 0) (def cust-id (get (get cust-list i) 0)) "")
      (recur (+ i 1))
    )
  )
  (if(not= cust-id "") 
    (loop [j 0]
      (when (< j (count sales-list))
        #_(if (= cust-id (get (get sales-list j) 1)) (def temp-vec (conj temp-vec [(get (get sales-list j) 2) (get (get sales-list j) 3)])) "")
        (if (= cust-id (get (get sales-list j) 1))
          (let [prod-id (get (get sales-list j) 2) prod-count (get (get sales-list j) 3)]
            (loop [k 0]
              (when (< k (count prod-list))
                (if (= prod-id (get (get prod-list k) 0))
                  (def total (* (+ total (parse-float (get (get prod-list k) 2))) (parse-float prod-count))
                  )
                )
                (recur (+ k 1))
              )
            )
          )
        )
        (recur (+ j 1))
      )
    ) 
  )
  (println input ": ""$" total)
  #_(if (> total 0.0) (println input ": ""$" total)"Wrong input")
)
(defn option-5 [cust-list prod-list sales-list]
  (println "Product Name : ")
  (def input (read-line))
  (def prod-id "")
  (def prod-count 0)
  (loop [i 0]
    (when (< i (count prod-list))
      (if (= (compare input (get (get prod-list i) 1)) 0) (def prod-id (get (get prod-list i) 0)) "")
      (recur (+ i 1))
    )
  )
  (loop [j 0]
    (when (< j (count sales-list))
      (if (= (compare prod-id (get (get sales-list j) 2)) 0)
        (def prod-count (+ prod-count (parse-int(get (get sales-list j) 3))))
      )
      (recur (+ j 1))
    )
  )
  (println input ":" prod-count)
)
(defn option-6 []
  (println "Good Bye!")
  (. System exit 0)
)

(defn main []

  (def cust-str (slurp "cust.txt"))
  (def prod-str (slurp "prod.txt"))
  (def sales-str (slurp "sales.txt"))
  (def cust-vec (clojure.string/split cust-str #"\n"))
  (def prod-vec (clojure.string/split prod-str #"\n"))
  (def sales-vec (clojure.string/split sales-str #"\n"))
  (def cust-size (count cust-vec))
  (def prod-size (count prod-vec))
  (def sales-size (count sales-vec))

  (def cust-list [])
  (def prod-list [])
  (def sales-list [])

  (loop[x 0]
    (when (< x  cust-size)
      (let [y (clojure.string/split (cust-vec x) #"\|")]
        (def cust-list (conj cust-list y))
      )
      (recur (+ x 1))
    )
  )
  (loop[x 0]
    (when (< x  prod-size)
      (let [y (clojure.string/split (prod-vec x) #"\|")]
        (def prod-list (conj prod-list y))
      )
      (recur (+ x 1))
    )
  )
  (loop[x 0]
    (when (< x  sales-size)
      (let [y (clojure.string/split (sales-vec x) #"\|")]
        (def sales-list (conj sales-list y))
      )
      (recur (+ x 1))
    )
  )
  (def cust-list (into [] (sort-by first cust-list)))
  (def prod-list (into [] (sort-by first prod-list)))
  (def sales-list (into [] (sort-by first sales-list)))
  

  (loop []
    (print-menu)
    (let [input (read-line)]
      (case input
        "1" (option-1 cust-list)
        "2" (option-2 prod-list)
        "3" (option-3 cust-list prod-list sales-list)
        "4" (option-4 cust-list prod-list sales-list)
        "5" (option-5 cust-list prod-list sales-list)
        "6" (option-6)
        ""
      )
    )
    (recur)
  )
)

(main)