; exercise 1
(defun bjunc (p q)
    (or (and p q) (and (not p) (not q))))
; exercise 2
(defun list-changer (list)
    (format t "~a ~%"
    (append (cdr list) (cons (car list) nil))))
; exercise 3
(defun func (x)
    (if (> (sin x) 0)
    (format t "~a ~%" (sin x))
    (format t "0")))
; exercise 4
(defparameter *nillist* nil)
(defun gen-list (num)
    (dotimes (x num)
        (push nil *nillist*)))
; exercise 5
(defun fib (x)
        (cond ((= x 0) 0)
              ((= x 1) 1)
              ((> x 1) (+ (fib (- x 2)) (fib (- x 1))))))
; exercise 6
; strange solution
(defun my-number (num thelist)
    (setf *newlist* (member num thelist))
	(push 't *newlist*)
	(if (= (length *newlist*) 1)
        (format t "~a ~%" (nth 1 *newlist*))
        (format t "~a ~%" (car *newlist*))))
; recuration way
(defparameter *newlist* nil)
(defun my-member (num thelist)
     (cond ((null thelist)
           (push nil *newlist*)
			(print nil))
          ((eq num (car thelist))
           (push t *newlist*)
		   (format t "T"))
          (t (my-member num (cdr thelist)))))
; exercise 7
(defun deep-member (at li)
    (cond ((null li) nil)
          ((eq at (car li)) T)
          (listp (car li))
                    (or (deep-member at (car li))
                    (deep-member at (cdr li))))
                (t (deep-member at (cdr li))))
; exercise 8
; loop way
(setq x 1)
(setq *sum* 0)
(defun binary-to-int (numlist)
    (if (null numlist)
        (print nil)
        (progn 
        (loop for x from 1 to (length numlist) do
            (setf *sum* (+ *sum* (* (expt 2 (- (length numlist) x)) (nth (- x 1) numlist)))))
        (format t "~a ~%" *sum*))))
; recursion way
(defun binary-to-init (numlist)
    (if (null numlist) 0
    ( + (* (car numlist) (expt 2 (- (length numlist) 1))) (binary-to-init (cdr numlist)))))
; exercise 9
(defparameter *binary* nil)
(defun int-to-binary (num)
    (if (eq num 0)
        (push 0 *binary*)
        (if (eq num 1)
            (push 1 *binary*)
            (progn
                (loop 
                    (if (eq (oddp num) T)
                        (progn
                            (setf num (floor (/ num 2)))
                            (push 1 *binary*))
                        (progn
                            (setf num (/ num 2))
                           (push 0 *binary*)))
                    (when (eq num 1) (return num)))
                (push 1 *binary*))))
    (print *binary*))
; exercise 10
(setq *print-case* :downcase)
(defparameter *justnothing* nil)
(defun add-elements (s n l)
    (progn 
        (dotimes (x (- n (length l)))
            (push s *justnothing*))
        (setf *newlist* (append *justnothing* l))
		(print *newlist*)
    ))