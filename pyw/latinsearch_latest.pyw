ó
}¨%Wc           @ s%  d  Z  d d l m Z m Z m Z d d l Z d d l Z y d d l Z Wn e	 k
 ri d d l Z n Xd d l
 Z
 d d l Z d d l m Z d d l m Z d d l m Z m Z m Z y d d l m Z Wn e	 k
 rë e Z n Xe j d d	 k r2d d l Z d d l Z d d l Z d d l Z nQ e j d d
 k rd d l Z d d l m Z d d l j Z d d l m  Z n  d Z! d Z" g  Z# e j$ j% d  Z& e j$ j% d  Z' e j$ j% d  Z( d Z) d Z* d Z+ d d d d d d d d d d d d  d! d" d# g Z, e-   a. d$ e! Z/ d% e! e" f Z0 d&   Z1 d'   Z2 d(   Z3 d)   Z4 d*   Z5 d+ e- f d,     YZ6 d- e- f d.     YZ7 d/ e- f d0     YZ8 d1 e- f d2     YZ9 d3 e- f d4     YZ: d5 e j; f d6     YZ< d7   Z= d8   Z> d9   Z? d:   Z@ eA d; k r!e?   n  d S(<   u   Latin Search programiÿÿÿÿ(   t   print_functiont   unicode_literalst   with_statementN(   t   SequenceMatcher(   t   Pool(   t   Processt   Valuet   Lock(   t   PrettyTablei    u   2u   3(   t   ttk(   t
   filedialogu   v0.2.0u   Jinu   data/latin_without_sougou.csvu   data/latin_60000.keys.pickleu   data/latin_60000.dict.pickleu   http://frps.eflora.cn/frps/i   g333333Ó?u   Ãu   ãu   ï¼u   ãu   ãu   îu   îu   <u   >u   *u   [u   @u   ]u   ï¼»u   |uå  
æ¤ç©æä¸åæç´¢ï¼Latin Namer Finerï¼

[ä»ç»]

    æ ¹æ®æ¤ç©æ¼é³ç¼©åãæ¼é³ãä¸­æåç§°æèæä¸åæç´¢æ¤ç©å¶ä»ä¿¡æ¯ã

    å¾å°åéè¯åï¼*åå»* åéè¯ï¼å°å¾å°è¯¦ç»ä¿¡æ¯ãå¦ææ²¡æå¹éï¼å°ä¼ä½¿ç¨ç³¢ç³æç´¢ã

[çæ¬]

    %s

[ä½¿ç¨æ¹æ³]

    1. ä½¿ç¨æ¼é³é¦å­æ¯æç´¢ãä¾å¦æç´¢ âeqxlmâï¼å°ä¼å¾å° âäºçæ¬éæ¨â
       åå¶ä»æ¬éæ¨ç¸å³çç»æã
    2. ä½¿ç¨æ¼é³å¨ç§°æç´¢ãä¾å¦æç´¢ âerqiuxuanlingmuâï¼å°ä¼å¾å° âäºçæ¬éæ¨â
       åå¶ä»æ¬éæ¨ç¸å³çç»æã
    3. ä½¿ç¨ä¸­ææç´¢ãä¾å¦æç´¢ âæ¬éæ¨âï¼å°ä¼å¾å° âäºçæ¬éæ¨âï¼ âä¸çæ¬éæ¨â
       ç­ç¸å³æç´¢ç»æã
    4. ä½¿ç¨æä¸åæç´¢ãä¾å¦æç´¢ âPlatanus Ã acerifoliaâï¼å°ä¼å¾å° âäºçæ¬éæ¨â
       ç¸å³çç»æã

[åéè¯ä»ç»]

    +---+------------------------+
    | 1 | åéè¯ä»¥æ¥è¯¢è¯å¼å§æç»å°¾
    |---+------------------------+
    | 2 | åéè¯åå«æ¥è¯¢è¯
    |---+------------------------+
    | 3 | æ ¹æ®ç¸ä¼¼æ§è¿è¡ç³¢ç³æç´¢
    |---+------------------------+
    | 4 | æ¼åæ£æ¥ï¼ç¼è¾è·ç¦»ä¸º 1)
    +---+------------------------+

u)  
============================================================
è½¯ä»¶åç§°ï¼æ¤ç©æä¸åæç´¢ï¼Latin Namer Finerï¼
è½¯ä»¶çæ¬ï¼%s
è½¯ä»¶ä½èï¼%s
ä½¿ç¨æ¹æ³ï¼è¯·ç¹å»èåæ ä¸­ "Help" - "Help" ä»¥æ¥çä½¿ç¨æ¹å¼ã
============================================================
c         C s&   t  |  d   } | j   SWd QXd S(   u%   Read file and return a list of lines.u   rN(   t   opent	   readlines(   t	   file_namet   f_in(    (    s   latinsearch.pyt	   get_linesm   s    c   
      C s  g  g  g  g  f \ } } } } g  } t  |  d  ¼ } x² | D]ª } t j d d k rh | j d  } n  g  | j d  D] } | j   ^ qx }	 | j |	 d  | j |	 d  | j |	 d  | j |	 d  | j t |	   q= WWd	 QX| | | | | f S(
   u  
    File:
        +-----+-------+------+----------------------+-------+
        | mg  | mugua | æ¨ç | Chaenomeles sinensis | Lynn. |
        +-----+-------+--- --+----------------------+-------+

    Processing:

        dict_1: {'mg': ('mg', 'mugua', 'æ¨ç', 'Chaenomeles sinensis', '')}
        dict_2: {'mugua': ('mg', 'mugua', 'æ¨ç', 'Chaenomeles sinensis', '')}
        dict_3: {'æ¨ç': ('mg', 'mugua', 'æ¨ç', 'Chaenomeles sinensis', '')}
        dict_4: {'Chaenomeles sinensis': ('mg', 'mugua',
                                          'æ¨ç', 'Chaenomeles sinensis', '')}

    Returns:
        (dict_1, dict_2, dict_3, dict_4)
    u   ri    u   2u   utf-8u   ,i   i   i   N(   R   t   syst   versiont   decodet   splitt   stript   appendt   tuple(
   R   t   column_list_1t   column_list_2t   column_list_3t   column_list_4t   detailed_info_tuple_listR   t   linet   xt   elements(    (    s   latinsearch.pyt   get_key_value_pairs_from_files   s    (	c         C sq   i  } xd t  t |  |   D]M \ } \ } } | | k rX g  | | <| | j |  q | | j |  q W| S(   u¨   
    Generate a dictionary from two lists. keys may be duplicated.

    >>> get_one_to_more_dict(['a', 'b', 'a', 'a'], [1, 2, 3, 4])
    {'a': [1, 3, 4], 'b': [2]}
    (   t	   enumeratet   zipR   (   t   key_listt
   value_listt	   _out_dictt   it   keyt   value(    (    s   latinsearch.pyt   get_one_to_more_dict   s    (
c          C s¯   t  t  \ }  } } } } t |  |  } t | |  } t | |  } t | |  } x- | | | f D] }	 |	 rg | j |	  qg qg Wt t |  | | |   }
 |
 | f S(   uC   Combine dicts, each with one column as key and whole line as value.(   R   t	   DATA_FILER(   t   updatet   listt   set(   R   R   R   R   R   t   dict_1t   dict_2t   dict_3t   dict_4t	   each_dictt   keys_for_all(    (    s   latinsearch.pyt   get_dict_for_all_columns¨   s    c         C s   t  d |  |  j   S(   un   Return similarity of two strings.

    [Example]
        >>> get_similarity('abcde', 'bcdef')
        0.8
    N(   R   t   Nonet   ratio(   t   str_at   str_b(    (    s   latinsearch.pyt   get_similarityÁ   s    t
   SpellCheckc           B sG   e  Z d  Z d   Z e d  Z d   Z d   Z d   Z d   Z	 RS(   uW  Train data set with given data then do spell check for given word.

    [Example]
        >>> s = SpellCheck(['abcd', 'fghi'])
        >>> s.correct('abci')
        'abcd'

    [Reference]
        [1]: Title:   How to Write a Spelling Corrector
             Author:  Peter Norvig
             Webpage: http://norvig.com/spell-correct.html
    c         C s:   | |  _  |  j   |  _ |  j d t  |  _ d |  _ d  S(   Nt   loweruB   abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.:1234567890(   t   candidate_listt   traint   NWORDSt   Truet   NWORDS_lowert   alphabet(   t   selfR;   (    (    s   latinsearch.pyt   __init__Ý   s    	c         C s   |  j  s t d   n  t j d    } | sW x[ |  j  D] } | | c d 7<q: Wn7 |  j  } x* t d   |  D] } | | c d 7<qt W| S(   u   Train model with data set.u*   Blank training list (Choosed blank file?).c           S s   d S(   Ni   (    (    (    (    s   latinsearch.pyt   <lambda>è   s    i   c         S s
   |  j    S(   N(   R:   (   t   _(    (    s   latinsearch.pyRC   î   s    (   R;   t
   ValueErrort   collectionst   defaultdictt   map(   RA   R:   t   modelt   ft   tmp_list(    (    s   latinsearch.pyR<   ä   s    	
c      	   C s  t  |  } t g  t |  D] } | d | !| | d ^ q g  t | d  D]3 } | d | !| | d | | | | d ^ qO g  t |  D]3 } |  j D]# } | d | !| | | d ^ q  q g  t | d  D]/ } |  j D] } | d | !| | | ^ qè qÛ  S(   u   Words that has one edit distance.

        1. deletion
        2. transposition
        3. alteration
        4. insertion
        i    i   i   (   t   lenR,   t   rangeR@   (   RA   t   wordt   nR%   t   c(    (    s   latinsearch.pyt   edits1ò   s    »c          s#   t    f d     j |  D  S(   u!   Words that has two edit distance.c         3 s@   |  ]6 }   j  |  D]  } | j     j k r | Vq q d  S(   N(   RQ   R:   R?   (   t   .0t   e1t   e2(   RA   (    s   latinsearch.pys	   <genexpr>  s    (   R,   RQ   (   RA   RN   (    (   RA   s   latinsearch.pyt   known_edits2  s    c          s   t    f d   | D  S(   u   Known words.c         3 s*   |  ]  } | j      j k r | Vq d  S(   N(   R:   R?   (   RR   t   w(   RA   (    s   latinsearch.pys	   <genexpr>  s    (   R,   (   RA   t   words(    (   RA   s   latinsearch.pyt   known	  s    c          sL     j  | g  p0   j    j |   p0 | g } t | d   f d   S(   u9   Do spell check and correct word if word was wrong spelledR&   c          s     j  |  S(   N(   R?   (   RV   (   RA   (    s   latinsearch.pyRC     s    (   RX   RQ   t   max(   RA   RN   t
   candidates(    (   RA   s   latinsearch.pyt   correct  s    *	(
   t   __name__t
   __module__t   __doc__RB   t   FalseR<   RQ   RU   RX   R[   (    (    (    s   latinsearch.pyR9   Ï   s   				t	   QueryWordc           B sw   e  Z d  Z d   Z e e d   Z e e d   Z e e d   Z e e d   Z	 e e e e f d  Z
 RS(   uè  Query with 4 strategy with multi-processing.

    [Strategies]

        1. Starts with              'abcde'.startswith('abc')
        2. Contains                 'bcd' in 'abcde'
        3. Rank by Similarity
        4. Spell check

    [turn_on_mode]

        Default: (True, True, True, True)
            Return all 4 results.

        (True, True, False, False)
            Return results of strategy_1 and strategy_2, and blank result
            of strategy_3 and strategy_4

    [Usage]

        query_object = QueryWord(keys_for_all, dict_for_all)

        # Startswith
        # query_object.get_starts_with_candidates(query)
        # Contains
        # query_object.get_contains_candidates(query)
        # Similarity
        # query_object.get_similar_candidates(query, limit=30)
        # Spell Check
        # query_object.get_spell_check_candidate(query)
        # All Four

        query_object.query_all_four(
            query,
            turn_on_mode=(True, True, True, True))
    c         C s\   g  | D] } | j    r | j    ^ q |  _ | |  _ t |  |  _ d |  _ i  |  _ d  S(   Nu    (   R   R2   t   dict_for_allR9   t   trained_objectt   queryt   result_dict(   RA   R2   Ra   R   (    (    s   latinsearch.pyRB   C  s    !		c   
      C sí   g  } | rÕ |  | k rx | j  |   | j |   d } x= | d  D]. } | j   rC | |  k rC | j  |  qC qC Wn  xZ t |  D]I \ } }	 |	 j |   s¯ |	 j |   r |	 |  k rÎ | j  |	  qÎ q q Wn  | j i | d 6 d S(   u   Check startswith & endswithi    i   u   0N(   R   t   getR   R    t
   startswitht   endswithR*   (
   Rc   R2   Ra   Rd   t   turn_ont	   _tmp_listt   result_elementst   eachR%   t	   candidate(    (    s   latinsearch.pyt   get_starts_with_candidatesN  s    c   
      C sÛ   g  } | rÃ |  | k rx | j  |   | j |   d } x= | d  D]. } | j   rC | |  k rC | j  |  qC qC Wn  xH t |  D]7 \ } }	 |  |	 k r |	 |  k r¼ | j  |	  q¼ q q Wn  | j i | d 6 d S(   u   Check containsi    i   u   1N(   R   Re   R   R    R*   (
   Rc   R2   Ra   Rd   Rh   Ri   Rj   Rk   R%   Rl   (    (    s   latinsearch.pyt   get_contains_candidatesg  s    c         C sâ   g  } g  } | rÊ t  | j d   d k rÊ xK t |  D]= \ } } t | |   }	 |	 t k r: | j |	 | f  q: q: W| j d d   d t  | t  } | rÁ g  | D] }
 |
 d ^ q« n g  } n  | j	 i | d 6 d S(	   u   Rank candidates by similarityu   1i    R&   c         S s   |  d S(   Ni    (    (   R   (    (    s   latinsearch.pyRC     s    t   reversei   u   2N(
   RL   Re   R    R8   t   SIMILARITY_THRESHOLDR   t   sortR>   t   SIMILAR_RESULT_NUM_LIMITR*   (   Rc   R2   Ra   Rd   Rh   Ri   t   _similar_hitsR%   Rl   t   _similarityRD   (    (    s   latinsearch.pyt   get_similar_candidates  s    !
,c         C sQ   d } | r9 t  | j d   d k r9 t j |   } n  | j i | d 6 d S(   u   Get spell check candicatesu    u   1i    u   3N(   RL   Re   t   TRAINED_OBJECTR[   R*   (   Rc   R2   Ra   Rd   Rh   Rl   (    (    s   latinsearch.pyt   get_spell_check_candidate  s    !c   	   
   C sõ   | |  _  i  } t j t j g } t j t j g } x\ t |  D]N \ } } t d | |  j  |  j |  j	 | | |   } | j
   | j   q@ Wx\ t |  D]N \ } } t d | |  j  |  j |  j	 | | |   } | j
   | j   q W| S(   u   Get four resultst   target(   Rc   R`   Rm   Rn   Ru   Rw   R    R   R2   Ra   t   startt   join(	   RA   Rc   t   turn_on_modeRd   t   func_list_1t   func_list_2R%   t	   each_funct   p(    (    s   latinsearch.pyt   query_all_four   s&    	

(   R\   R]   R^   RB   t   staticmethodR>   Rm   Rn   Ru   Rw   R   (    (    (    s   latinsearch.pyR`     s   $		t   RightClickMenuc           B s_   e  Z d  Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z	 d   Z
 d	   Z RS(
   u5  
    Simple widget to add basic right click menus to entry widgets.

    usage:

    rclickmenu = RightClickMenu(some_entry_widget)
    some_entry_widget.bind("<3>", rclickmenu)

    If you prefer to import Tkinter over Tix, just replace all Tix
    references with Tkinter and this will still work fine.
    c          sQ   |   _    j  j d   f d   d d   j  j d   f d   d d d  S(   Nu   <Control-a>c          s
     j    S(   N(   t   _select_all(   t   e(   RA   (    s   latinsearch.pyRC   à  s    t   addu   +u   <Control-A>c          s
     j    S(   N(   R   (   R   (   RA   (    s   latinsearch.pyRC   á  s    (   t   parentt   bind(   RA   R   (    (   RA   s   latinsearch.pyRB   Ú  s    	"c         C s:   |  j  j d  d k r d  S|  j  j   |  j |  d  S(   Nu   stateu   disable(   R   t   cgett   focus_forcet
   build_menu(   RA   t   event(    (    s   latinsearch.pyt   __call__ã  s    c         C sD  t  j |  j d d } |  j j   sV | j d d d d  | j d d d d  n2 | j d d d |  j  | j d d d |  j  |  j   r° | j d d	 d |  j  n | j d d	 d d  |  j j   sî | j d d
 d d  n | j d d
 d |  j	  | j
   | j d d d |  j  | j | j | j  d S(   u   Build right click menut   tearoffi    t   labelu   Copyt   stateu   disableu   Cutt   commandu   Pasteu   Deleteu
   Select AllN(   t   tkt   MenuR   t   selection_presentt   add_commandt   _copyt   _cutt   paste_string_statet   _pastet   _cleart   add_separatorR   t   postt   x_roott   y_root(   RA   R   t   menu(    (    s   latinsearch.pyR   ì  s    
c         C s   |  j  j d  d  S(   Nu   <<Cut>>(   R   t   event_generate(   RA   (    (    s   latinsearch.pyR     s    c         C s   |  j  j d  d  S(   Nu   <<Copy>>(   R   R   (   RA   (    (    s   latinsearch.pyR     s    c         C s   |  j  j d  d  S(   Nu	   <<Paste>>(   R   R   (   RA   (    (    s   latinsearch.pyR     s    c         C s   |  j  j d  d  S(   Nu	   <<Clear>>(   R   R   (   RA   (    (    s   latinsearch.pyR     s    c         C s'   |  j  j d d  |  j  j d  d S(   Ni    u   endu   break(   R   t   selection_ranget   icursor(   RA   (    (    s   latinsearch.pyR     s    c         C s(   y |  j  j d d  } Wn t SXt S(   u,   Returns true if a string is in the clipboardt	   selectionu	   CLIPBOARD(   R   t   selection_getR_   R>   (   RA   t	   clipboard(    (    s   latinsearch.pyR   #  s
    (   R\   R]   R^   RB   R   R   R   R   R   R   R   R   (    (    (    s   latinsearch.pyR   Í  s   					"						t   RightClickMenuForListBoxc           B s2   e  Z d  Z d   Z d   Z d   Z d   Z RS(   u9  
    Simple widget to add basic right click menus to entry widgets.

    usage:

    rclickmenu = RightClickMenuForListBox(listbox_widget)
    listbox_widget.bind("<3>", rclickmenu)

    If you prefer to import Tkinter over Tix, just replace all Tix
    references with Tkinter and this will still work fine.
    c         C s   | |  _  d  S(   N(   R   (   RA   R   (    (    s   latinsearch.pyRB   =  s    c         C s:   |  j  j d  d k r d  S|  j  j   |  j |  d  S(   Nu   stateu   disable(   R   R   R   R   (   RA   R   (    (    s   latinsearch.pyR   @  s    c         C sK   t  j |  j d d } | j d d d |  j  | j | j | j  d S(   u   Build right click menuR   i    R   u   CopyR   N(   R   R   R   R   R   R   R   R   (   RA   R   R   (    (    s   latinsearch.pyR   I  s    c         C s   |  j  j d  d  S(   Nu   <<Copy>>(   R   R   (   RA   (    (    s   latinsearch.pyR   O  s    (   R\   R]   R^   RB   R   R   R   (    (    (    s   latinsearch.pyR¥   0  s
   				t   RightClickMenuForScrolledTextc           B sh   e  Z d  Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z	 d   Z
 d	   Z d
   Z RS(   u>   Simple widget to add basic right click menus to entry widgets.c          sQ   |   _    j  j d   f d   d d   j  j d   f d   d d d  S(   Nu   <Control-a>c          s
     j    S(   N(   R   (   R   (   RA   (    s   latinsearch.pyRC   \  s    R   u   +u   <Control-A>c          s
     j    S(   N(   R   (   R   (   RA   (    s   latinsearch.pyRC   ]  s    (   R   R   (   RA   R   (    (   RA   s   latinsearch.pyRB   V  s    	"c         C s=   |  j  j d  t j k r d  S|  j  j   |  j |  d  S(   Nu   state(   R   R   R   t   DISABLEDR   R   (   RA   R   (    (    s   latinsearch.pyR   _  s    c         C s÷   t  j |  j d d } | j d d d |  j  | j d d d |  j  |  j   rr | j d d d |  j  n | j d d d d	  | j d d
 d |  j  | j	   | j d d d |  j
  | j d d d |  j  | j | j | j  d S(   u
   build menuR   i    R   u   CopyR   u   Cutu   PasteR   u   disableu   Deleteu
   Select Allu	   Clear AllN(   R   R   R   R   R   R   t   _paste_string_statet   _paste_if_string_in_clipboardt   _deleteR   R   t
   _clear_allR   R   R   (   RA   R   R   (    (    s   latinsearch.pyR   h  s    
c         C s   |  j  j d  d  S(   Nu   <<Cut>>(   R   R   (   RA   (    (    s   latinsearch.pyR     s    c         C s   |  j  j d  d  S(   Nu   <<Copy>>(   R   R   (   RA   (    (    s   latinsearch.pyR     s    c         C s   |  j  j d  d  S(   Nu	   <<Clear>>(   R   R   (   RA   (    (    s   latinsearch.pyRª     s    c         C s   |  j  j d  d  S(   Nu	   <<Paste>>(   R   R   (   RA   (    (    s   latinsearch.pyR©     s    c         C s=   |  j  j d d d  |  j  j d d  |  j  j d  d S(   u
   select allu   selu   1.0u   end-1cu   insertu   break(   R   t   tag_addt   mark_sett   see(   RA   (    (    s   latinsearch.pyR     s    c         C s(   y |  j  j d d  } Wn t SXt S(   u,   Returns true if a string is in the clipboardR¢   u	   CLIPBOARD(   R   R£   R_   R>   (   RA   R¤   (    (    s   latinsearch.pyR¨     s
    c         C s   |  j  j d d  d S(   u	   Clear allu   1.0u   endN(   R   t   delete(   RA   (    (    s   latinsearch.pyR«   ¨  s    (   R\   R]   R^   RB   R   R   R   R   Rª   R©   R   R¨   R«   (    (    (    s   latinsearch.pyR¦   S  s   					!						t   AutocompleteGUIc           B s¼   e  Z d  Z d g  i  d  Z d   Z d   Z d   Z d   Z d   Z	 d   Z
 d   Z d	   Z e d
  Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z RS(   u&   The main GUI for autocomplete program.c         C s   t  j j |  |  | |  _ | |  _ g  |  _ |  j j   |  j   |  j	   |  j
   |  j   |  j   |  j   |  j j d  |  j j d t  d  S(   Nu   1400x800u   Latin Finder %s(   R   t   FrameRB   R2   Ra   t   historyt   mastert   gridt	   set_stylet   create_menu_bart   create_widgetst   grid_configuret   create_right_menut	   bind_funct   geometryt   titlet   __version__(   RA   R³   R2   Ra   (    (    s   latinsearch.pyRB   °  s    			





c         C s\   t  j   } | j d d d | j d d d | j d d d | j d	 d d
 d S(   u)   Set style for widgets in the main window.u	   TComboboxt   paddingi   u   auto.TComboboxt
   foregroundu   redu   TButtoni
   u   open.TButtonu   blueN(   R	   t   Stylet	   configure(   RA   t   s(    (    s   latinsearch.pyRµ   ¿  s
    c         C sÚ  t  j |  j  |  _ t  j |  j d d |  _ |  j j d d d |  j  |  j j   |  j j d d d |  j j  |  j j	 d d d |  j  t  j |  j d d } | j d d	 d |  j
  | j d d
 d |  j  |  j   r| j d d d |  j  n | j d d d d    | j d d d |  j  |  j j	 d d d |  t  j |  j d d |  _ |  j j d d d |  j  |  j j d d d |  j  |  j j	 d d d |  j  |  j j d |  j  d S(   u#   Create menubar for the main window.R   i    R   u   Save result to file...R   u   Exitu   FileR   u   Copyu   Cutu   Pastec           S s
   t  d  S(   Nu   No string in clipboard!(   t   print(    (    (    s   latinsearch.pyRC   è  s    u   Deleteu   Editu   Helpu   AboutN(   R   R   R³   t   menubart	   file_menuR   t   _ask_save_fileR   t   quitt   add_cascadeR   R   R¨   R   Rª   t	   help_menut   _display_helpt   _display_aboutt   config(   RA   t	   edit_menu(    (    s   latinsearch.pyR¶   Ç  s6    
	

c      
    sñ  t  j   j d d   _   j j d d d d d t j t j t j t j	  t  j
   j d d   _ t j   j d	 d    _ t  j   j    _ t  j
   j d d   _ t j   j d	 d!   _ t  j   j    _ t  j
   j d d   _ t j   j d	 d"   _ t  j   j    _ t  j
   j d d   _ t j   j d	 d#   _ t  j   j    _ t  j
   j d d   _ t j   j d	 d$   _ t  j   j d d   _   j j d d d d d d d t j t j    j j   t  j    j d d d d   _!   j! j d d d d d d d t j    j j d d d d d d d t j    j j d d d d d t j t j t j t j	    j j d d d d d t j t j	    j j" d   j j#    j j" d   j j$    j j d d d d d d d t j    j j d d d d d t j t j t j t j	    j j d d d d d t j t j	    j j" d   j j#    j j" d   j j$    j j d d d d d d d t j    j j d d d d d t j t j t j t j	    j j d d d d d t j t j	    j j" d   j j#    j j" d   j j$    j j d d d d d d d t j    j j d d d d d t j t j t j t j	    j j d d d d d t j t j	    j j" d   j j#    j j" d   j j$    j j d d d d d d d t j    j j d d d d d d d t j t j	 t j t j    j%     f d   } x0   j   j   j   j g D] } | |  qÙWd S(%   u'   Create widgets for the main GUI window.R¾   i   t   rowi    t   columnt   stickyt   textu"   Candidates (Startswith / Endswith)t   fontu	   Monospacei
   u   Candidates (Contains)u   Candidates (Rank by similarity)u.   Candidates (Spell check, single edit distance)u]   Click "Do Query" button and see results. ** Double Click ** candidate to see detailed result.t   styleu   auto.TComboboxt
   columnspani   u   Do Queryu   copy.TButtoni   i   t   yscrollcommandR   i   i   i   i   c          s<     j  d    f d    t    }   j  d |  d S(   u¤   Bind command to listbox.

            Double click on candidates from any column from the four,
            then the result will be on the output area.
            u   <Double-Button-1>c          s     j    S(   N(   t   _display_search_result(   R   (   RA   t   widget(    s   latinsearch.pyRC   ^  s    u
   <Button-3>N(   R   R¥   (   R×   t   right_menu_widget(   RA   (   R×   s   latinsearch.pyt   bind_command_to_listboxR  s    	N(   u	   Monospacei
   (   u	   Monospacei
   (   u	   Monospacei
   (   u	   Monospacei
   (   u	   Monospacei
   (&   R	   R±   R³   t   contentR´   R   t   Wt   Et   Nt   St   Labelt   label_1t   Listboxt   listbox1t	   Scrollbart
   scrollbar1t   label_2t   listbox2t
   scrollbar2t   label_3t   listbox3t
   scrollbar3t   label_4t   listbox4t
   scrollbar4t   label_5t   stt   ScrolledTextt   scrolled_text_5t   Comboboxt	   input_boxt   focust   Buttont   do_query_buttonRÌ   R,   t   yviewRÊ   (   RA   RÙ   t   listbox(    (   RA   s   latinsearch.pyR·   ø  s    7			/	
(7)(7)(7)(7)(
c         C sN  |  j  j d d d |  j  j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d	 d d d
 S(   u)   Grid configuration of window and widgets.i    t   weighti   i   i   i   i   i   i   N(   R³   t   rowconfiguret   columnconfigureRÚ   (   RA   (    (    s   latinsearch.pyR¸   g  s    c         C sH   t  |  j  } |  j j d |  t |  j  } |  j j d |  d  S(   Nu
   <Button-3>(   R   Ró   R   R¦   Rñ   (   RA   t   right_menu_input_boxt   right_menu_scrolled_text_5(    (    s   latinsearch.pyR¹   z  s
    c         C s   |  j  |  j d <d  S(   Nu   command(   t   _display_candidatesRö   (   RA   (    (    s   latinsearch.pyRº     s    c         C s  |  j  j   j   } t |  j |  j  } i g  d 6g  d 6g  d 6d d 6} | r| |  j k r | j | d t t t t f } qd | k rµ | j | d t t t t f } q| d t	 j
 k rì | j | d t t t t f } q| j | d t t t t f } n  | S(	   u0   Command of Do Query button with multi-processingu   0u   1u   2u    u   3R{   u    i    (   Ró   Re   R   R`   R2   Ra   R   R>   R_   t   stringt	   printable(   RA   Rc   t   query_word_objectRd   (    (    s   latinsearch.pyt	   _do_query  s*    "c         C së   |  j    } |  j j d d  x% | d D] } |  j j d |  q* W|  j j d d  x% | d D] } |  j j d |  qe W|  j j d d  x% | d D] } |  j j d |  q  W|  j j d d  |  j j d | d  d  S(   Nu   0u   endu   1u   2u   3(   R  Râ   R¯   t   insertRæ   Ré   Rì   (   RA   Rd   t   item(    (    s   latinsearch.pyRþ   ³  s    c         C sÆ  | j  d  } |  j j d t j  |  j j t j |  |  j j d d  |  j j  |  } | rÂt rVt d d d d d	 d
 d g  } x d D] } d | j	 | <q Wd | _
 x | D]{ } g  | d j   D] } | t k rÒ | ^ qÒ }	 t d j |	  }
 g  | D] } | ^ q
} | j |
  | j |  q» W|  j j d | j    qÂ|  j j d d d d  xN | D]C } d j |  } |  j j d |  |  j j d d d d  qxWn  d S(   u2   Clean content in Output Area and insert new value.u   activei    u   0.1u   end-1cu   Short Pinyinu   Long Pinyinu   Chineseu   Latinu   Nameru   Data Sourceu   Web URLu   li   i   u   %20u   endu[  è¯·å®è£ prettytable ä»¥è·å¾æ´æ¸æ°çç»æè§å¾ã
å®è£æ¹æ³ï¼ pip install prettytable

+--------------+-------------+---------+-------+-------+-------------+---------+
| Short Pinyin | Long Pinyin | Chinese | Latin | Namer | Data Source | Web URL |
+--------------+-------------+---------+-------+-------+-------------+---------+

%s
u   =id   u     |  u   
%s
u   -N(   u   Short Pinyinu   Long Pinyinu   Chineseu   Latinu   Nameru   Data Sourceu   Web URL(   Re   Ró   R¯   R   t   ENDR  Rñ   Ra   R   t   alignt   padding_widthR   t   SPECIAL_CHARSt   FRPS_BASE_URLRz   R   t   add_rowt
   get_string(   RA   R×   t   is_clean_wordt   selection_valuet   resultt   tableRÏ   t   each_resultR   t   normal_word_listt   urlRD   RK   R   (    (    s   latinsearch.pyRÖ   È  s<    	
		c         C s   |  j  j   j d  d  S(   Nu   <<Copy>>(   R³   t	   focus_getR   (   RA   (    (    s   latinsearch.pyR   ÷  s    c         C s   |  j  j   j d  d  S(   Nu   <<Cut>>(   R³   R  R   (   RA   (    (    s   latinsearch.pyR   ü  s    c         C s   |  j  j   j d  d  S(   Nu	   <<Paste>>(   R³   R  R   (   RA   (    (    s   latinsearch.pyR     s    c         C s   |  j  j   j d  d  S(   Nu	   <<Clear>>(   R³   R  R   (   RA   (    (    s   latinsearch.pyRª     s    c         C s(   y |  j  j d d  } Wn t SXt S(   u,   Returns true if a string is in the clipboardR¢   u	   CLIPBOARD(   R³   R£   R_   R>   (   RA   R¤   (    (    s   latinsearch.pyR¨   	  s
    c         C ss   t  j d d d d  } | d k r( d S|  j j d d  j d  } | j | j d  j d	   | j   d S(
   u   Dialog to open file.t   modeu   wt   defaultextensionu   .txtNu   1.0u   end-1cu   GBKu   utf-8(	   t   tkFileDialogt   asksaveasfileR4   Rñ   Re   t   encodet   writeR   t   close(   RA   RJ   t   text_to_save(    (    s   latinsearch.pyRÆ     s    c         C s*   |  j  j d d  |  j  j d t  d  S(   Nu   0.1u   end-1cu   end(   Rñ   R¯   R  t
   USAGE_INFO(   RA   (    (    s   latinsearch.pyRÊ     s    c         C s*   |  j  j d d  |  j  j d t  d  S(   Nu   0.1u   end-1cu   end(   Rñ   R¯   R  t
   ABOUT_INFO(   RA   (    (    s   latinsearch.pyRË   "  s    N(   R\   R]   R^   R4   RB   Rµ   R¶   R·   R¸   R¹   Rº   R  Rþ   R>   RÖ   R   R   R   Rª   R¨   RÆ   RÊ   RË   (    (    (    s   latinsearch.pyR°   ­  s&   		1	o		
		(	/								c         C s{   t    \ }  } t j |   } t j |  } t t d   } | j |  Wd QXt t d   } | j |  Wd QXd S(   ub   Dump generated dictinary to pickle raw file.

    Generally, this function need only do once.
    u   wbN(   R3   t   picklet   dumpsR   t   PICKLE_KEYS_FILER  t   PICKLE_DICT_FILE(   R2   Ra   t   pickle_keyst   pickle_dictt   f_out(    (    s   latinsearch.pyt   dump_with_pickle'  s    c         C sp   t  |  d  " } | j   } t j |  } Wd QXt  | d  " } | j   } t j |  } Wd QX| | f S(   u'   Load keys and dict from pickle raw fileu   rbN(   R   t   readR  t   loads(   t   pickle_keys_filet   pickle_dict_fileR   R"  R2   R#  Ra   (    (    s   latinsearch.pyt   load_with_pickle5  s    c          C sD   t  t t  \ }  } t |   a t d |  d |  } | j   d S(   u   The main GUI program.R2   Ra   N(   R*  R   R!  R9   Rv   R°   t   mainloop(   R2   Ra   t   app(    (    s   latinsearch.pyt   gui_mainB  s    	c           C s   t    d S(   u	   Main funcN(   R3   (    (    (    s   latinsearch.pyt   mainQ  s    u   __main__(B   R^   t
   __future__R    R   R   t   osR   t   cPickleR  t   ImportErrorRÿ   RF   t   difflibR   t   multiprocessingR   R   R   R   t   prettytableR   R4   R   t   TkinterR   R	   R  Rð   Rï   t   tkintert   tkinter.scrolledtextt   scrolledtextR
   R½   t
   __author__t   _historyt   patht   abspathR)   R   R!  R	  Rr   Rp   R  t   objectRv   R  R  R   R   R(   R3   R8   R9   R`   R   R¥   R¦   R±   R°   R%  R*  R-  R.  R\   (    (    (    s   latinsearch.pyt   <module>   st   
	&
			#			N°c#Zÿ {				